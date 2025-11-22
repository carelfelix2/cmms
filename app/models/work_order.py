from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.sql import func
from app.database.connection import Base


class WorkOrder(Base):
    __tablename__ = "work_orders"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    asset_id = Column(Integer, ForeignKey("assets.id"), nullable=True)
    created_by = Column(Integer, ForeignKey("users.id"), nullable=True)
    status = Column(String, default="open")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
