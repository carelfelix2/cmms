from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database.connection import get_db
from app.schemas.work_order import WorkOrderCreate, WorkOrderResponse
from app.services.work_order_service import WorkOrderService

router = APIRouter()


@router.post("/", response_model=WorkOrderResponse)
def create_work_order(payload: WorkOrderCreate, db: Session = Depends(get_db)):
    svc = WorkOrderService(db)
    return svc.create(payload)


@router.get("/", response_model=List[WorkOrderResponse])
def list_work_orders(db: Session = Depends(get_db)):
    svc = WorkOrderService(db)
    return svc.list()


@router.get("/{wo_id}", response_model=WorkOrderResponse)
def get_work_order(wo_id: int, db: Session = Depends(get_db)):
    svc = WorkOrderService(db)
    wo = svc.get(wo_id)
    if not wo:
        raise HTTPException(status_code=404, detail="Work order not found")
    return wo
