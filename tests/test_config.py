from src.config import DevConfig, ProdConfig, TestConfig, config


def test_dev_config():
    cfg = DevConfig()
    assert cfg.DATABASE_URL is not None


def test_prod_config():
    cfg = ProdConfig()
    assert cfg.DATABASE_URL is not None


def test_test_config():
    cfg = TestConfig()
    assert cfg.DATABASE_URL is not None


def test_get_config():
    cfg = config
    assert cfg.DATABASE_URL is not None
