from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database.connection import get_db
from app.schemas.preventive_maintenance import PMCreate, PMResponse
from app.repositories.preventive_maintenance_repository import PreventiveMaintenanceRepository

router = APIRouter()


@router.post("/", response_model=PMResponse)
def create_pm(payload: PMCreate, db: Session = Depends(get_db)):
    repo = PreventiveMaintenanceRepository(db)
    return repo.create_pm(payload)


@router.get("/", response_model=List[PMResponse])
def list_pm(db: Session = Depends(get_db)):
    repo = PreventiveMaintenanceRepository(db)
    return repo.list_pm()


@router.get("/{pm_id}", response_model=PMResponse)
def get_pm(pm_id: int, db: Session = Depends(get_db)):
    repo = PreventiveMaintenanceRepository(db)
    pm = repo.get_pm(pm_id)
    if not pm:
        raise HTTPException(status_code=404, detail="PM not found")
    return pm
