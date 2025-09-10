from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from ..database import get_session
from ..models import Transaction
from ..services.allocation import run_allocations

router = APIRouter()


@router.get("/totals/by-center")
def totals_by_center(period: str, session: Session = Depends(get_session)):
    rows = session.exec(select(Transaction).where(Transaction.period == period)).all()
    totals: dict[int, float] = {}
    for r in rows:
        totals[r.cost_center_id] = totals.get(r.cost_center_id, 0.0) + r.amount
    return totals


@router.get("/totals/by-object")
def totals_by_object(period: str, session: Session = Depends(get_session)):
    rows = session.exec(select(Transaction).where(Transaction.period == period)).all()
    totals: dict[int, float] = {}
    for r in rows:
        if r.cost_object_id is None:
            continue
        totals[r.cost_object_id] = totals.get(r.cost_object_id, 0.0) + r.amount
    return totals


@router.post("/allocate/{period}")
def allocate(period: str, session: Session = Depends(get_session)):
    created = run_allocations(period, session)
    return {"created": len(created)}