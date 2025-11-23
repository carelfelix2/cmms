from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database.connection import get_db
from app.schemas.asset import AssetCreate, AssetResponse, AssetUpdate
from app.services.asset_service import AssetService

router = APIRouter()


@router.post("/", response_model=AssetResponse)
def create_asset(payload: AssetCreate, db: Session = Depends(get_db)):
    svc = AssetService(db)
    return svc.create_asset(payload)


@router.get("/", response_model=List[AssetResponse])
def list_assets(db: Session = Depends(get_db)):
    svc = AssetService(db)
    return svc.get_assets()


@router.get("/{asset_id}", response_model=AssetResponse)
def get_asset(asset_id: int, db: Session = Depends(get_db)):
    svc = AssetService(db)
    asset = svc.get_asset_by_id(asset_id)
    if not asset:
        raise HTTPException(status_code=404, detail="Asset not found")
    return asset


@router.put("/{asset_id}", response_model=AssetResponse)
def update_asset(asset_id: int, payload: AssetUpdate, db: Session = Depends(get_db)):
    svc = AssetService(db)
    updated = svc.update_asset(asset_id, payload)
    if not updated:
        raise HTTPException(status_code=404, detail="Asset not found")
    return updated


@router.delete("/{asset_id}")
def delete_asset(asset_id: int, db: Session = Depends(get_db)):
    svc = AssetService(db)
    deleted = svc.delete_asset(asset_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Asset not found")
    return {"deleted": asset_id}
