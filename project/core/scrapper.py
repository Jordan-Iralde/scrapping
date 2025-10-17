import requests
from time import sleep
from core.utils import retry
from core.logger import get_logger

logger = get_logger(__name__)

@retry(retries=3, delay=2)
def fetch_page(url: str) -> str:
    """Descarga una página HTML con manejo de errores."""
    logger.info(f"Descargando: {url}")
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()
    return response.text

def scrape_data() -> list[str]:
    """Scrapea múltiples páginas y devuelve sus HTMLs."""
    urls = [
        "https://listado.mercadolibre.com.ar/"
    ]

    html_pages = []
    for url in urls:
        try:
            html = fetch_page(url)
            html_pages.append(html)
            sleep(1)  # para no saturar el servidor
        except Exception as e:
            logger.error(f"Error al descargar {url}: {e}")
    return html_pages
