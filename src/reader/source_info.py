from dataclasses import dataclass

from src.reader.source_config import SourceConfig


@dataclass
class SourceInfo:
    name: str
    config: SourceConfig
