from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from ..database import get_session
from ..models import CostElement

router = APIRouter()


@router.get("/", response_model=list[CostElement])
def list_cost_elements(session: Session = Depends(get_session)):
    return session.exec(select(CostElement)).all()


@router.post("/", response_model=CostElement)
def create_cost_element(data: CostElement, session: Session = Depends(get_session)):
    exists = session.exec(select(CostElement).where(CostElement.code == data.code)).first()
    if exists:
        raise HTTPException(status_code=400, detail="Cost element code already exists")
    session.add(data)
    session.commit()
    session.refresh(data)
    return data


@router.get("/{element_id}", response_model=CostElement)
def get_cost_element(element_id: int, session: Session = Depends(get_session)):
    obj = session.get(CostElement, element_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    return obj


@router.put("/{element_id}", response_model=CostElement)
def update_cost_element(element_id: int, data: CostElement, session: Session = Depends(get_session)):
    obj = session.get(CostElement, element_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    obj.code = data.code
    obj.name = data.name
    obj.is_primary = data.is_primary
    session.add(obj)
    session.commit()
    session.refresh(obj)
    return obj


@router.delete("/{element_id}")
def delete_cost_element(element_id: int, session: Session = Depends(get_session)):
    obj = session.get(CostElement, element_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    session.delete(obj)
    session.commit()
    return {"ok": True}