import json
from dataclasses import dataclass, asdict


@dataclass
class SourceConfig:
    host: str
    port: int
    database: str
    username: str
    password: str
    ssl: bool

    def to_dict(self):
        return asdict(self)
    def to_json(self):
        return json.dumps(self.to_dict())
