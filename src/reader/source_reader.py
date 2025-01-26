import airbyte as ab

from src.config import get_settings
from src.reader.source_config import SourceConfig
from src.reader.source_info import SourceInfo

config = get_settings()


class SourceReader:
    def get_connectors(self):
        return ab.get_available_connectors()

    def get_source_config(self):
        src_cfg = SourceConfig()
        src_cfg.database = config.DEV_SOURCE_DB
        src_cfg.host = config.DEV_SOURCE_HOST
        src_cfg.port = config.DEV_SOURCE_PORT
        src_cfg.username = config.DEV_SOURCE_USER
        src_cfg.password = config.DEV_SOURCE_PASS
        src_cfg.ssl = config.DEV_SOURCE_SSL

        src_info = SourceInfo()
        src_info.name = config.DEV_SOURCE
        src_info.config = src_cfg

        return src_info
