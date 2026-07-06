from fastapi import FastAPI
from app.core.config import settings

from app.db.database import engine

from sqlalchemy import text
from app.db.database import engine
from app.api.organizations import router as organization_router


app = FastAPI(
    title="TeamFlow API",
    version="0.1.0",
    description="Production-grade project management backend"
)

app.include_router(organization_router)

@app.get("/health")
def health_check():
    return {"status": "ok", "service": "teamflow-api"}

