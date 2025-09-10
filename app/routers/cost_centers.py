from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from ..database import get_session
from ..models import CostCenter

router = APIRouter()


@router.get("/", response_model=list[CostCenter])
def list_cost_centers(session: Session = Depends(get_session)):
    return session.exec(select(CostCenter)).all()


@router.post("/", response_model=CostCenter)
def create_cost_center(data: CostCenter, session: Session = Depends(get_session)):
    exists = session.exec(select(CostCenter).where(CostCenter.code == data.code)).first()
    if exists:
        raise HTTPException(status_code=400, detail="Cost center code already exists")
    session.add(data)
    session.commit()
    session.refresh(data)
    return data


@router.get("/{center_id}", response_model=CostCenter)
def get_cost_center(center_id: int, session: Session = Depends(get_session)):
    obj = session.get(CostCenter, center_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    return obj


@router.put("/{center_id}", response_model=CostCenter)
def update_cost_center(center_id: int, data: CostCenter, session: Session = Depends(get_session)):
    obj = session.get(CostCenter, center_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    obj.code = data.code
    obj.name = data.name
    obj.parent_id = data.parent_id
    session.add(obj)
    session.commit()
    session.refresh(obj)
    return obj


@router.delete("/{center_id}")
def delete_cost_center(center_id: int, session: Session = Depends(get_session)):
    obj = session.get(CostCenter, center_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    session.delete(obj)
    session.commit()
    return {"ok": True}