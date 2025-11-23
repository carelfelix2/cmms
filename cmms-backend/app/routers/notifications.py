from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.database.connection import get_db
from app.schemas.notification import NotificationCreate, NotificationResponse
from app.services.notification_service import NotificationService

router = APIRouter()


@router.get("/", response_model=List[NotificationResponse])
def list_notifications(db: Session = Depends(get_db)):
    svc = NotificationService(db)
    return svc.list()


@router.post("/", response_model=NotificationResponse)
def create_notification(payload: NotificationCreate, db: Session = Depends(get_db)):
    svc = NotificationService(db)
    return svc.create(payload)
