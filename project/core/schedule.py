import schedule
import time
from main import main
from core.logger import get_logger

logger = get_logger(__name__)

def schedule_job():
    schedule.every().day.at("10:00").do(main)
    logger.info("Scraper programado todos los días a las 10:00 AM")

    while True:
        schedule.run_pending()
        time.sleep(60)
