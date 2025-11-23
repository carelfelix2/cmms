from sqlalchemy import Column, Integer, String, Text, ForeignKey
from app.database.connection import Base


class Asset(Base):
    __tablename__ = "assets"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    tag = Column(String, unique=True, index=True, nullable=True)
    location = Column(String, nullable=True)
    description = Column(Text, nullable=True)
    vendor_id = Column(Integer, ForeignKey("vendors.id"), nullable=True)
