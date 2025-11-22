from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class NotificationCreate(BaseModel):
    title: str
    message: Optional[str] = None
    level: Optional[str] = "info"


class NotificationResponse(NotificationCreate):
    id: int
    created_at: Optional[datetime]

    class Config:
        orm_mode = True
