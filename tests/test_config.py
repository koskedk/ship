import logging
import os

import pytest
from pydantic_settings import SettingsConfigDict

from src.config import GlobalConfig

# Check if running in GitHub Actions
IN_GITHUB_ACTIONS = os.getenv("GITHUB_ACTIONS") == "true"

# Configure logging
logging.basicConfig(level=logging.INFO)


@pytest.mark.skipif(IN_GITHUB_ACTIONS, reason="Integration tests")
@pytest.mark.parametrize("mode", ["DEV_", "TEST_", "PROD_"])
def test_dev_config(mode):
    cfg = get_new_config(mode)

    assert cfg.DATABASE_URL is not None
    logging.info(cfg.DATABASE_URL)


def get_new_config(prefix: str):
    class Config(GlobalConfig):
        model_config = SettingsConfigDict(
            env_file="tests\\.env.test", env_prefix=prefix
        )

    return Config()
