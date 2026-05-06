from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    secret_key: str = "changeme-super-secret-key-for-dev-only"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 1440  # 24 hours
    database_url: str = "sqlite:///./game_dev.db"
    cors_origins: List[str] = ["http://localhost:4200"]

    model_config = {"env_file": ".env"}


settings = Settings()
