from loguru import logger

import airbyte as ab

from src.config import get_settings
from src.reader.source_config import SourceConfig
from src.reader.source_info import SourceInfo

config = get_settings()


class SourceReader:
    def get_connectors(self):
        print(ab.caches.get_default_cache().cache_dir)
        return ab.get_available_connectors()

    def get_source_config(self):
        src_cfg = SourceConfig(
            config.SOURCE_HOST,
            config.SOURCE_PORT,
            config.SOURCE_DB,
            config.SOURCE_USER,
            config.SOURCE_PASS,
            config.SOURCE_SSL
        )

        src_info = SourceInfo(config.SOURCE, src_cfg)

        logger.info(f"Source info: {src_info.config}")
        logger.info(f"Source info: {src_info.config.database}")
        logger.info(f"Source info: {src_info.config.host}")
        return src_info

    def read(self):
        cfg = self.get_source_config()

        src = ab.get_source(
            cfg.name,
            config=cfg.config.to_json())
        src.check()
        return True
