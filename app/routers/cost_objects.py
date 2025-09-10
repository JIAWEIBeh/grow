from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from ..database import get_session
from ..models import CostObject

router = APIRouter()


@router.get("/", response_model=list[CostObject])
def list_cost_objects(session: Session = Depends(get_session)):
    return session.exec(select(CostObject)).all()


@router.post("/", response_model=CostObject)
def create_cost_object(data: CostObject, session: Session = Depends(get_session)):
    exists = session.exec(select(CostObject).where(CostObject.code == data.code)).first()
    if exists:
        raise HTTPException(status_code=400, detail="Cost object code already exists")
    session.add(data)
    session.commit()
    session.refresh(data)
    return data


@router.get("/{obj_id}", response_model=CostObject)
def get_cost_object(obj_id: int, session: Session = Depends(get_session)):
    obj = session.get(CostObject, obj_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    return obj


@router.put("/{obj_id}", response_model=CostObject)
def update_cost_object(obj_id: int, data: CostObject, session: Session = Depends(get_session)):
    obj = session.get(CostObject, obj_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    obj.code = data.code
    obj.name = data.name
    obj.type = data.type
    session.add(obj)
    session.commit()
    session.refresh(obj)
    return obj


@router.delete("/{obj_id}")
def delete_cost_object(obj_id: int, session: Session = Depends(get_session)):
    obj = session.get(CostObject, obj_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    session.delete(obj)
    session.commit()
    return {"ok": True}