from sqlalchemy.orm import Session
from app.models.asset import Asset
from app.schemas.asset import AssetCreate, AssetUpdate


class AssetRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_asset(self, asset: AssetCreate):
        db_asset = Asset(**asset.dict())
        self.db.add(db_asset)
        self.db.commit()
        self.db.refresh(db_asset)
        return db_asset

    def get_assets(self):
        return self.db.query(Asset).all()

    def get_asset_by_id(self, asset_id: int):
        return self.db.query(Asset).filter(Asset.id == asset_id).first()

    def update_asset(self, asset_id: int, asset_update: AssetUpdate):
        db_asset = self.get_asset_by_id(asset_id)
        if not db_asset:
            return None
        for key, value in asset_update.dict(exclude_unset=True).items():
            setattr(db_asset, key, value)
        self.db.commit()
        self.db.refresh(db_asset)
        return db_asset

    def delete_asset(self, asset_id: int):
        db_asset = self.get_asset_by_id(asset_id)
        if not db_asset:
            return None
        self.db.delete(db_asset)
        self.db.commit()
        return db_asset
