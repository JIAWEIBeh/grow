from sqlmodel import Session
from .database import engine
from .models import CostCenter, CostElement, CostObject, CostObjectType, Transaction, AllocationRule, AllocationMethod


def seed() -> None:
    with Session(engine) as session:
        # Cost Centers
        cc_admin = CostCenter(code="CC-ADMIN", name="Admin")
        cc_mfg = CostCenter(code="CC-MFG", name="Manufacturing")
        cc_sales = CostCenter(code="CC-SALES", name="Sales")
        session.add_all([cc_admin, cc_mfg, cc_sales])
        session.commit()
        session.refresh(cc_admin); session.refresh(cc_mfg); session.refresh(cc_sales)

        # Cost Elements
        ce_salary = CostElement(code="CE-SAL", name="Salaries", is_primary=True)
        ce_oh = CostElement(code="CE-OH", name="Overhead", is_primary=False)
        ce_hours = CostElement(code="DRV-HRS", name="Labor Hours Driver", is_primary=True)
        session.add_all([ce_salary, ce_oh, ce_hours])
        session.commit()
        session.refresh(ce_salary); session.refresh(ce_oh); session.refresh(ce_hours)

        # Cost Objects
        obj_prod_a = CostObject(code="PROD-A", name="Product A", type=CostObjectType.PRODUCT)
        obj_prod_b = CostObject(code="PROD-B", name="Product B", type=CostObjectType.PRODUCT)
        session.add_all([obj_prod_a, obj_prod_b])
        session.commit()
        session.refresh(obj_prod_a); session.refresh(obj_prod_b)

        # Primary transactions for period
        txns = [
            Transaction(period="2025-08", cost_center_id=cc_admin.id, cost_element_id=ce_salary.id, amount=10000.0, description="Admin salaries"),
            Transaction(period="2025-08", cost_center_id=cc_mfg.id, cost_element_id=ce_salary.id, amount=30000.0, description="Mfg salaries"),
            Transaction(period="2025-08", cost_center_id=cc_sales.id, cost_element_id=ce_salary.id, amount=20000.0, description="Sales salaries"),
            # Driver measures (hours) in same period
            Transaction(period="2025-08", cost_center_id=cc_mfg.id, cost_element_id=ce_hours.id, amount=600.0, description="Mfg hours"),
            Transaction(period="2025-08", cost_center_id=cc_sales.id, cost_element_id=ce_hours.id, amount=400.0, description="Sales hours"),
        ]
        session.add_all(txns)
        session.commit()

        # Allocation rules
        # 30% of Admin salaries to Sales; remainder driver-based to Mfg/Sales by hours
        rules = [
            AllocationRule(
                period="2025-08",
                source_cost_center_id=cc_admin.id,
                source_cost_element_id=ce_salary.id,
                method=AllocationMethod.PERCENTAGE,
                percentage=0.3,
                target_cost_center_id=cc_sales.id,
            ),
            AllocationRule(
                period="2025-08",
                source_cost_center_id=cc_admin.id,
                source_cost_element_id=ce_salary.id,
                method=AllocationMethod.DRIVER,
                driver_cost_element_id=ce_hours.id,
            ),
        ]
        session.add_all(rules)
        session.commit()


if __name__ == "__main__":
    seed()