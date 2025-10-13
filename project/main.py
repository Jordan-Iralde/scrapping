import yaml
import pandas as pd
from core.scraper import MercadoLibreScraper
from core.sheets_uploader import GoogleSheetsUploader
from core.logger import setup_logger

def main():
    logger = setup_logger()
    logger.info("=== Iniciando scraper de Mercado Libre ===")

    # Leer configuración
    with open("config.yaml", "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    scraper = MercadoLibreScraper(
        base_url=config["base_url"],
        query=config["search_query"],
        max_pages=config["max_pages"],
        delay=tuple(config["delay_seconds"]),
        logger=logger
    )

    items = scraper.scrape()
    if not items:
        logger.warning("No se encontraron resultados.")
        return

    df = pd.DataFrame(items)
    df.to_csv("data/output.csv", index=False)
    logger.info(f"Datos guardados localmente: data/output.csv ({len(df)} filas)")

    try:
        gs = GoogleSheetsUploader(
            spreadsheet_name=config["google_sheets"]["spreadsheet_name"],
            worksheet_name=config["google_sheets"]["worksheet_name"]
        )
        gs.upload_dataframe(df)
        logger.info("Datos subidos correctamente a Google Sheets.")
    except Exception as e:
        logger.error(f"Error al subir a Google Sheets: {e}")

    logger.info("✅ Scraping completado exitosamente")

if __name__ == "__main__":
    main()
