from pydantic import BaseModel
from typing import Optional


class AssetBase(BaseModel):
    name: str
    tag: Optional[str] = None
    location: Optional[str] = None
    description: Optional[str] = None


class AssetCreate(AssetBase):
    vendor_id: Optional[int] = None


class AssetUpdate(BaseModel):
    name: Optional[str] = None
    location: Optional[str] = None
    description: Optional[str] = None


class AssetResponse(AssetBase):
    id: int
    vendor_id: Optional[int] = None

    model_config = {
        "from_attributes": True
    }
