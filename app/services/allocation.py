from typing import Iterable
from sqlmodel import Session, select
from ..models import AllocationRule, Transaction, AllocationMethod


def run_allocations(period: str, session: Session) -> list[Transaction]:
    rules: list[AllocationRule] = session.exec(
        select(AllocationRule).where((AllocationRule.period == period) | (AllocationRule.period.is_(None)))
    ).all()

    created: list[Transaction] = []

    for rule in rules:
        source_txns = session.exec(
            select(Transaction).where(
                Transaction.period == period,
                Transaction.cost_center_id == rule.source_cost_center_id,
                Transaction.cost_element_id == rule.source_cost_element_id,
            )
        ).all()
        if not source_txns:
            continue

        total_amount = sum(t.amount for t in source_txns)
        if total_amount == 0:
            continue

        if rule.method == AllocationMethod.PERCENTAGE:
            if rule.percentage is None or rule.target_cost_center_id is None:
                continue
            amount = total_amount * float(rule.percentage)
            if amount == 0:
                continue
            txn = Transaction(
                period=period,
                cost_center_id=rule.target_cost_center_id,
                cost_element_id=rule.source_cost_element_id,
                cost_object_id=None,
                amount=amount,
                description=f"Allocation from CC {rule.source_cost_center_id} {total_amount} * {rule.percentage}",
            )
            session.add(txn)
            created.append(txn)
        elif rule.method == AllocationMethod.DRIVER:
            if rule.driver_cost_element_id is None:
                continue
            driver_txns = session.exec(
                select(Transaction).where(
                    Transaction.period == period,
                    Transaction.cost_element_id == rule.driver_cost_element_id,
                )
            ).all()
            driver_totals_by_cc: dict[int, float] = {}
            for dt in driver_txns:
                driver_totals_by_cc[dt.cost_center_id] = driver_totals_by_cc.get(dt.cost_center_id, 0.0) + dt.amount
            driver_total = sum(driver_totals_by_cc.values())
            if driver_total == 0:
                continue
            for target_cc_id, driver_amount in driver_totals_by_cc.items():
                share = driver_amount / driver_total
                amount = total_amount * share
                if amount == 0:
                    continue
                txn = Transaction(
                    period=period,
                    cost_center_id=target_cc_id,
                    cost_element_id=rule.source_cost_element_id,
                    cost_object_id=None,
                    amount=amount,
                    description=f"Driver allocation share {share:.4f} of {total_amount}",
                )
                session.add(txn)
                created.append(txn)

    session.commit()
    for t in created:
        session.refresh(t)
    return created