"""Health check endpoint."""

from fastapi import APIRouter
from pydantic import BaseModel

from voice_agent import __version__

router = APIRouter(tags=["health"])


class HealthResponse(BaseModel):
    """Response model for the health check endpoint."""

    status: str = "healthy"
    version: str = __version__


@router.get("/health", response_model=HealthResponse)
async def health_check() -> HealthResponse:
    """Return the application health status."""
    return HealthResponse(status="healthy", version=__version__)
