from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database.connection import engine, Base

from app.routers import (
    auth,
    assets,
    work_orders,
    preventive_maintenance,
    notifications,
    vendors,
    dashboard,
)


def create_app() -> FastAPI:
    app = FastAPI(title="CMMS Hospital Backend", version="1.0.0")

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
    app.include_router(assets.router, prefix="/assets", tags=["Asset Management"])
    app.include_router(work_orders.router, prefix="/work-orders", tags=["Work Order Management"])
    app.include_router(preventive_maintenance.router, prefix="/pm", tags=["Preventive Maintenance"])
    app.include_router(notifications.router, prefix="/notifications", tags=["Notifications"])
    app.include_router(vendors.router, prefix="/vendors", tags=["Vendor Management"])
    app.include_router(dashboard.router, prefix="/dashboard", tags=["Dashboard"])

    @app.on_event("startup")
    def on_startup():
        # Create tables for the simple skeleton
        Base.metadata.create_all(bind=engine)

    @app.get("/")
    def read_root():
        return {"message": "Welcome to CMMS Hospital Backend"}

    return app


app = create_app()
