from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class WorkOrderBase(BaseModel):
    title: str
    description: Optional[str] = None


class WorkOrderCreate(WorkOrderBase):
    asset_id: Optional[int] = None


class WorkOrderResponse(WorkOrderBase):
    id: int
    asset_id: Optional[int]
    status: str
    created_at: Optional[datetime]

    class Config:
        orm_mode = True
