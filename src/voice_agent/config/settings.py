"""Application settings loaded from environment variables / .env file."""

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application configuration.

    Values are read from environment variables, falling back to a local
    ``.env`` file, and finally to the defaults defined here.
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # ── Application ─────────────────────────────────────────
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8000
    LOG_LEVEL: str = "INFO"

    # ── CORS ────────────────────────────────────────────────
    # Comma-separated list of allowed origins, or "*" for any origin.
    CORS_ALLOW_ORIGINS: str = "*"

    @property
    def cors_origins(self) -> list[str]:
        """Parse ``CORS_ALLOW_ORIGINS`` into a list of origins."""
        return [o.strip() for o in self.CORS_ALLOW_ORIGINS.split(",") if o.strip()]


@lru_cache
def get_settings() -> Settings:
    """Return a cached settings singleton."""
    return Settings()
