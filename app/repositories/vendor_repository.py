from sqlalchemy.orm import Session
from app.models.vendor import Vendor
from app.schemas.vendor import VendorCreate


class VendorRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_vendor(self, v: VendorCreate):
        db_v = Vendor(**v.dict())
        self.db.add(db_v)
        self.db.commit()
        self.db.refresh(db_v)
        return db_v

    def list_vendors(self):
        return self.db.query(Vendor).all()

    def get_vendor(self, vendor_id: int):
        return self.db.query(Vendor).filter(Vendor.id == vendor_id).first()
