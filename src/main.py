from fastapi import FastAPI
from loguru import logger

from src.startup import add_logging

add_logging()

logger.info("starting livesync.ship...")
app = FastAPI(title="livesync.ship")
logger.error("NOT LICENSE FOUND !")
logger.info("livesync.ship started !")


@app.get("/")
async def index():
    logger.info("xxxx")
    return {"status": "ship is alive"}
