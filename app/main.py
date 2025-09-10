from fastapi import FastAPI
from .database import init_db
from .routers import cost_centers, cost_elements, cost_objects, transactions, reporting


def create_app() -> FastAPI:
    app = FastAPI(title="Cost Accounting Prototype", version="0.1.0")
    init_db()
    app.include_router(cost_centers.router, prefix="/api/cost-centers", tags=["cost-centers"])
    app.include_router(cost_elements.router, prefix="/api/cost-elements", tags=["cost-elements"])
    app.include_router(cost_objects.router, prefix="/api/cost-objects", tags=["cost-objects"])
    app.include_router(transactions.router, prefix="/api/transactions", tags=["transactions"])
    app.include_router(reporting.router, prefix="/api/reporting", tags=["reporting"])
    return app


app = create_app()