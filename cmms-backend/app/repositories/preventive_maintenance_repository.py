from sqlalchemy.orm import Session
from app.models.preventive_maintenance import PreventiveMaintenance
from app.schemas.preventive_maintenance import PMCreate


class PreventiveMaintenanceRepository:
    def __init__(self, db: Session):
        self.db = db

    def list_pm(self):
        return self.db.query(PreventiveMaintenance).all()

    def get_pm(self, pm_id: int):
        return self.db.query(PreventiveMaintenance).filter(PreventiveMaintenance.id == pm_id).first()

    def create_pm(self, pm: PMCreate):
        db_pm = PreventiveMaintenance(**pm.dict())
        self.db.add(db_pm)
        self.db.commit()
        self.db.refresh(db_pm)
        return db_pm
