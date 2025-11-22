from app.repositories.work_order_repository import WorkOrderRepository
from app.schemas.work_order import WorkOrderCreate


class WorkOrderService:
    def __init__(self, db):
        self.repo = WorkOrderRepository(db)

    def create(self, wo: WorkOrderCreate, created_by: int = None):
        return self.repo.create_work_order(wo, created_by)

    def list(self):
        return self.repo.get_work_orders()

    def get(self, wo_id: int):
        return self.repo.get_work_order_by_id(wo_id)
