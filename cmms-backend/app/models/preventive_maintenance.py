from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.sql import func
from app.database.connection import Base


class PreventiveMaintenance(Base):
    __tablename__ = "preventive_maintenances"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    asset_id = Column(Integer, ForeignKey("assets.id"), nullable=True)
    frequency = Column(String, nullable=True)
    next_due = Column(DateTime, nullable=True)
    notes = Column(Text, nullable=True)
