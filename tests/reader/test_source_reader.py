import logging
import json
from dataclasses import asdict

from src.reader.source_reader import SourceReader

logging.basicConfig(level=logging.INFO)

reader = SourceReader()

def test_get_connectors():

    list = reader.get_connectors()
    assert len(list) > 0
    for cn in list:
        logging.info(cn)

def test_get_source_config():
    cfg=reader.get_source_config();
    assert cfg.name is not None
    assert cfg.config.database is not None
    logging.info(f" >>>>>>>>>>>>>>>>>> {cfg.name} <<<<<<<<<<<<")
    logging.info(f" >>>>>>>>>>>>>>>>>> {cfg.config.to_json()} <<<<<<<<<<<<")

def test_read():
    assert reader.read()