import sys

from loguru import logger


def add_logging():
    logger.remove()
    logger.add(
        sys.stdout,
        colorize=True,
        format=(
            "<green>{time:YYYY-MM-DD HH:mm:ss}</green> |"
            "<level>{level: <8}</level> |"
            "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
            "<level>{message}</level>"
        ),
    )
    logger.add(
        "error.log",
        colorize=True,
        format=(
            "<red>{time:YYYY-MM-DD HH:mm:ss}</red> |"
            "<level>{level: <8}</level> |"
            "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
            "<level>{message}</level>"
        ),
        level="ERROR",
        rotation="1 week",
    )
