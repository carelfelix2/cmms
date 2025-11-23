from pydantic import BaseModel
from typing import Optional


class VendorBase(BaseModel):
    name: str
    contact: Optional[str] = None
    phone: Optional[str] = None


class VendorCreate(VendorBase):
    notes: Optional[str] = None


class VendorResponse(VendorBase):
    id: int

    class Config:
        orm_mode = True
