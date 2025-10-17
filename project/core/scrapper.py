import requests
import time
from core.utils import retry, load_config
from core.logger import get_logger
from playwright.sync_api import sync_playwright

logger = get_logger(__name__)
config = load_config()

HEADERS = config["scraper"]["default_headers"]
DELAY = config["scraper"]["delay"]
SITES = config["scraper"]["sites"]

@retry(retries=config["scraper"]["retries"], delay=2)
def fetch_static(url: str) -> str:
    """Descarga una página HTML estática."""
    logger.info(f"Descargando (estático): {url}")
    response = requests.get(url, headers=HEADERS, timeout=10)
    response.raise_for_status()
    return response.text

def fetch_dynamic(url: str, wait_time: int = 5) -> str:
    """Usa Playwright para páginas con JavaScript."""
    logger.info(f"Descargando (dinámico): {url}")
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=True)
        page = browser.new_page()
        page.goto(url)
        time.sleep(wait_time)  # esperar que se renderice JS
        html = page.content()
        browser.close()
    return html

def scrape_data() -> list[dict]:
    """Scrapea múltiples sitios configurados y devuelve los HTMLs."""
    results = []
    for site in SITES:
        base_url = site["url"]
        use_js = site.get("use_js", False)
        pages = site.get("pages", 1)
        wait_time = site.get("wait_time", 5)

        for i in range(1, pages + 1):
            url = base_url.format(i) if "{}" in base_url else base_url
            try:
                html = fetch_dynamic(url, wait_time) if use_js else fetch_static(url)
                results.append({"site": site["name"], "url": url, "html": html})
                time.sleep(DELAY)
            except Exception as e:
                logger.error(f"Error al descargar {url}: {e}")
    return results
