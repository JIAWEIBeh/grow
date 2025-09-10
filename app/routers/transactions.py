from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from ..database import get_session
from ..models import Transaction

router = APIRouter()


@router.get("/", response_model=list[Transaction])
def list_transactions(period: str | None = None, session: Session = Depends(get_session)):
    statement = select(Transaction)
    if period:
        statement = statement.where(Transaction.period == period)
    return session.exec(statement).all()


@router.post("/", response_model=Transaction)
def create_transaction(data: Transaction, session: Session = Depends(get_session)):
    session.add(data)
    session.commit()
    session.refresh(data)
    return data


@router.get("/{txn_id}", response_model=Transaction)
def get_transaction(txn_id: int, session: Session = Depends(get_session)):
    obj = session.get(Transaction, txn_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    return obj


@router.put("/{txn_id}", response_model=Transaction)
def update_transaction(txn_id: int, data: Transaction, session: Session = Depends(get_session)):
    obj = session.get(Transaction, txn_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    obj.period = data.period
    obj.cost_center_id = data.cost_center_id
    obj.cost_element_id = data.cost_element_id
    obj.cost_object_id = data.cost_object_id
    obj.amount = data.amount
    obj.description = data.description
    session.add(obj)
    session.commit()
    session.refresh(obj)
    return obj


@router.delete("/{txn_id}")
def delete_transaction(txn_id: int, session: Session = Depends(get_session)):
    obj = session.get(Transaction, txn_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    session.delete(obj)
    session.commit()
    return {"ok": True}