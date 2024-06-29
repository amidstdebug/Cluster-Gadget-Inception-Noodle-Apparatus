from fastapi import APIRouter
from src.api.routes import healthcheck, inference

api_router = APIRouter()
api_router.include_router(healthcheck.router, tags=["health"])
api_router.include_router(inference.router, tags=["procurement"])