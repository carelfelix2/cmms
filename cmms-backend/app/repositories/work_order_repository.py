from sqlalchemy.orm import Session
from app.models.work_order import WorkOrder
from app.schemas.work_order import WorkOrderCreate


class WorkOrderRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_work_order(self, wo: WorkOrderCreate, created_by: int = None):
        db_wo = WorkOrder(title=wo.title, description=wo.description, asset_id=wo.asset_id, created_by=created_by)
        self.db.add(db_wo)
        self.db.commit()
        self.db.refresh(db_wo)
        return db_wo

    def get_work_orders(self):
        return self.db.query(WorkOrder).all()

    def get_work_order_by_id(self, wo_id: int):
        return self.db.query(WorkOrder).filter(WorkOrder.id == wo_id).first()
