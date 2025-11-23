from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class PMBase(BaseModel):
    name: str
    frequency: Optional[str] = None


class PMCreate(PMBase):
    asset_id: Optional[int] = None


class PMResponse(PMBase):
    id: int
    next_due: Optional[datetime]

    class Config:
        orm_mode = True
