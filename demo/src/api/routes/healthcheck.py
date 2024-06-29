from fastapi import APIRouter, status
from src.interface.heartbeat import HealthCheckResult
from src.core.config import API_VERSION

router = APIRouter()

@router.get("/ping", response_model=HealthCheckResult, name="healthcheck")
async def get_heartbeat() -> HealthCheckResult:
    health_status = HealthCheckResult(body="Image Relevance endpoint is ok.", api_ver=API_VERSION)
    return health_status