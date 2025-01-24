import pytest
from pydantic_settings import SettingsConfigDict

from src.config import GlobalConfig


@pytest.mark.parametrize("mode", ["DEV_", "TEST_", "PROD_"])
def test_dev_config(mode):
    cfg = get_new_config(mode)

    assert cfg.DATABASE_URL is not None


def get_new_config(prefix: str):
    class Config(GlobalConfig):
        model_config = SettingsConfigDict(
            env_file="tests\\.env.test", env_prefix=prefix
        )

    return Config()
