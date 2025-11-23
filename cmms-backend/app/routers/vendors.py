from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database.connection import get_db
from app.schemas.vendor import VendorCreate, VendorResponse
from app.repositories.vendor_repository import VendorRepository

router = APIRouter()


@router.post("/", response_model=VendorResponse)
def create_vendor(payload: VendorCreate, db: Session = Depends(get_db)):
    repo = VendorRepository(db)
    return repo.create_vendor(payload)


@router.get("/", response_model=List[VendorResponse])
def list_vendors(db: Session = Depends(get_db)):
    repo = VendorRepository(db)
    return repo.list_vendors()


@router.get("/{vendor_id}", response_model=VendorResponse)
def get_vendor(vendor_id: int, db: Session = Depends(get_db)):
    repo = VendorRepository(db)
    v = repo.get_vendor(vendor_id)
    if not v:
        raise HTTPException(status_code=404, detail="Vendor not found")
    return v
