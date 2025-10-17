from core.scrapper import scrape_data
from core.parser import parse_html
from core.storage import save_to_csv
from core.logger import get_logger

logger = get_logger(__name__)

def main():
    logger.info("Iniciando el proceso de scraping...")

    html_pages = scrape_data()
    logger.info(f"Se descargaron {len(html_pages)} páginas HTML")

    df = parse_html(html_pages)
    logger.info(f"Se extrajeron {len(df)} filas de datos")

    save_to_csv(df, "data/processed/datos.csv")
    logger.info("Datos guardados en data/processed/datos.csv")


if __name__ == "__main__":
    main()
