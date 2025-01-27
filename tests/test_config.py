import logging
import os

from src.config import get_env_file, get_settings

# Configure logging
logging.basicConfig(level=logging.INFO)
os.environ["MODE"] = "testing"

get_settings.cache_clear()


def test_get_env_file():
    filename = get_env_file("testing")
    assert filename == ".env.testing"


def test_get_settings():
    cfg = get_settings("testing")
    logging.info(cfg.model_dump())
    assert cfg.DATABASE_URL == "sqlite:///test.db"
