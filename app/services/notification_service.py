from app.repositories.notification_repository import NotificationRepository
from app.schemas.notification import NotificationCreate


class NotificationService:
    def __init__(self, db):
        self.repo = NotificationRepository(db)

    def list(self):
        return self.repo.list_notifications()

    def create(self, payload: NotificationCreate):
        return self.repo.create_notification(payload)
