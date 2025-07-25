from pydantic_settings import BaseSettings
from enum import Enum


class Settings(BaseSettings):
    version: str = "1.1.7.9"
    environment: str = "prod"
    debug: bool = False
    cors_origins: list[str] = ["*"]

settings = Settings()
