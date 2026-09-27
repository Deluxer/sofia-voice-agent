"""Aggregate all API routers into a single router."""

from fastapi import APIRouter

from voice_agent.api.v1 import health

api_router = APIRouter()
api_router.include_router(health.router)
