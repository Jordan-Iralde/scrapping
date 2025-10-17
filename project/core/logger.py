import logging
import os

def get_logger(name: str):
    os.makedirs("data/logs", exist_ok=True)

    logging.basicConfig(
        filename="data/logs/scraper.log",
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )

    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    console.setFormatter(logging.Formatter("%(levelname)s - %(message)s"))

    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.addHandler(console)

    return logger
