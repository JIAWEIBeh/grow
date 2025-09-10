from __future__ import annotations
from enum import Enum
from typing import Optional
from sqlmodel import SQLModel, Field


class AllocationMethod(str, Enum):
    PERCENTAGE = "percentage"
    DRIVER = "driver"


class CostCenter(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    code: str = Field(index=True, unique=True)
    name: str
    parent_id: Optional[int] = Field(default=None, foreign_key="costcenter.id")


class CostElement(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    code: str = Field(index=True, unique=True)
    name: str
    is_primary: bool = Field(default=True, description="Primary or secondary cost element")


class CostObjectType(str, Enum):
    ORDER = "order"
    PRODUCT = "product"
    PROJECT = "project"


class CostObject(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    code: str = Field(index=True, unique=True)
    name: str
    type: CostObjectType = Field(default=CostObjectType.ORDER)


class Transaction(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    period: str = Field(index=True, description="YYYY-MM")
    cost_center_id: int = Field(foreign_key="costcenter.id")
    cost_element_id: int = Field(foreign_key="costelement.id")
    cost_object_id: Optional[int] = Field(default=None, foreign_key="costobject.id")
    amount: float
    description: Optional[str] = None


class AllocationRule(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    period: Optional[str] = Field(default=None, index=True)
    source_cost_center_id: int = Field(foreign_key="costcenter.id")
    source_cost_element_id: int = Field(foreign_key="costelement.id")
    method: AllocationMethod = Field(default=AllocationMethod.PERCENTAGE)
    percentage: Optional[float] = Field(default=None, description="0-1 for percentage allocations")
    driver_cost_element_id: Optional[int] = Field(default=None, foreign_key="costelement.id")
    target_cost_center_id: Optional[int] = Field(default=None, foreign_key="costcenter.id")