from sqlalchemy.orm import Session
from app.models.notification import Notification
from app.schemas.notification import NotificationCreate


class NotificationRepository:
    def __init__(self, db: Session):
        self.db = db

    def list_notifications(self):
        return self.db.query(Notification).all()

    def create_notification(self, payload: NotificationCreate):
        db_n = Notification(**payload.dict())
        self.db.add(db_n)
        self.db.commit()
        self.db.refresh(db_n)
        return db_n
