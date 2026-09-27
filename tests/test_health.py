"""Tests for the health check endpoint."""

from fastapi.testclient import TestClient

from voice_agent import __version__
from voice_agent.main import create_app

client = TestClient(create_app())


def test_health_check() -> None:
    """The health endpoint returns a healthy status and the app version."""
    response = client.get("/api/v1/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy", "version": __version__}
