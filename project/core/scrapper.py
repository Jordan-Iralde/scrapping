import requests
from core.utils import retry, random_delay
from core.parser import parse_items

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/117.0.0.0 Safari/537.36"
}

class MercadoLibreScraper:
    def __init__(self, base_url, query, max_pages=1, delay=(1.5, 3.5), logger=None):
        self.base_url = base_url
        self.query = query
        self.max_pages = max_pages
        self.delay = delay
        self.logger = logger
        self.session = requests.Session()
        self.session.headers.update(HEADERS)

    @retry(max_retries=5, delay=2)
    def get_page(self, url):
        resp = self.session.get(url, timeout=15)
        resp.raise_for_status()
        return resp.text

    def scrape(self):
        all_items = []
        for page in range(1, self.max_pages + 1):
            search_url = f"{self.base_url}{self.query}_Desde_{(page-1)*50 + 1}"
            if self.logger:
                self.logger.info(f"Scrapeando página {page}: {search_url}")
            html = self.get_page(search_url)
            items = parse_items(html)
            if self.logger:
                self.logger.info(f"Encontrados {len(items)} productos en página {page}.")
            all_items.extend(items)
            random_delay(*self.delay)
        return all_items
