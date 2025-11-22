from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.connection import get_db

router = APIRouter()


@router.get("/overview")
def overview(db: Session = Depends(get_db)):
    # Simple aggregate placeholders
    return {"assets": 0, "work_orders_open": 0, "pm_due": 0}
