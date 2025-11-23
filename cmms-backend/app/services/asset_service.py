from app.repositories.asset_repository import AssetRepository
from app.schemas.asset import AssetCreate, AssetUpdate


class AssetService:
    def __init__(self, db):
        self.repo = AssetRepository(db)

    def create_asset(self, asset: AssetCreate):
        return self.repo.create_asset(asset)

    def get_assets(self):
        return self.repo.get_assets()

    def get_asset_by_id(self, asset_id: int):
        return self.repo.get_asset_by_id(asset_id)

    def update_asset(self, asset_id: int, asset_update: AssetUpdate):
        return self.repo.update_asset(asset_id, asset_update)

    def delete_asset(self, asset_id: int):
        return self.repo.delete_asset(asset_id)
