from dataclasses import dataclass


@dataclass
class SourceConfig:
    host: str
    port: int
    database: str
    username: str
    password: str
    ssl: bool
