from fastapi import FastAPI
from loguru import logger

from src.config import get_settings
from src.startup import add_logging

add_logging()
config = get_settings()

logger.info("starting livesync.ship...")
app = FastAPI(title="livesync.ship")
logger.error("NOT LICENSE FOUND !")


logger.info(f"livesync.ship started [{config.DATABASE_URL}]!")


@app.get("/")
async def index():
    logger.info("xxxx")
    return {"status": "ship is alive"}
