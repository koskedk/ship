import os
from functools import lru_cache
from typing import Optional

from loguru import logger
from pydantic_settings import BaseSettings, SettingsConfigDict


def get_env_file(env_mode: Optional[str] = None):
    mode = os.getenv("MODE")
    if env_mode:
        mode = env_mode
    if not mode or mode.lower() == "production":
        file = ".env"
    else:
        file = f".env.{mode}".lower()
    logger.info(f"running in {mode} >> {file}")
    return file


class AppSettings(BaseSettings):
    MODE: Optional[str] = None
    DATABASE_URL: Optional[str] = None
    SOURCE: Optional[str] = None
    SOURCE_DB: Optional[str] = None
    SOURCE_HOST: Optional[str] = None
    SOURCE_PORT: Optional[int] = None
    SOURCE_USER: Optional[str] = None
    SOURCE_PASS: Optional[str] = None
    SOURCE_SSL: Optional[bool] = None
    DESTINATION: Optional[str] = None
    DESTINATION_DB: Optional[str] = None
    DESTINATION_HOST: Optional[str] = None
    DESTINATION_PORT: Optional[int] = None
    DESTINATION_USER: Optional[str] = None
    DESTINATION_PASS: Optional[str] = None
    DESTINATION_SSL: Optional[bool] = None
    model_config = SettingsConfigDict(extra="ignore")


@lru_cache()
def get_settings(env_mode: Optional[str] = None):
    return AppSettings(_env_file=(get_env_file(env_mode)))
