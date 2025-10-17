from core.scrapper import scrape_data
from core.parser import parse_html
from core.storage import save_to_csv_by_site
from core.logger import get_logger

logger = get_logger(__name__)

def main():
    logger.info("Iniciando el proceso de scraping...")
    
    html_results = scrape_data()
    logger.info(f"Se descargaron {len(html_results)} páginas HTML")
    
    site_dfs = parse_html(html_results)
    logger.info(f"Se parsearon {sum(len(df) for df in site_dfs.values())} filas en total")
    
    save_to_csv_by_site(site_dfs)
    logger.info("Datos guardados en archivos separados por sitio")

if __name__ == "__main__":
    main()
