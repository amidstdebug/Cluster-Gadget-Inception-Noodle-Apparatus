from pydantic import BaseModel

class HealthCheckResult(BaseModel):
    body: str
    api_ver: str