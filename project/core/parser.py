from bs4 import BeautifulSoup
import pandas as pd
from core.logger import get_logger

logger = get_logger(__name__)

def parse_books(html: str) -> list[dict]:
    soup = BeautifulSoup(html, "html.parser")
    books = soup.select("article.product_pod")
    data = []
    for book in books:
        title = book.h3.a["title"]
        price = book.select_one("p.price_color").get_text(strip=True)
        stock = book.select_one("p.instock.availability").get_text(strip=True)
        data.append({"title": title, "price": price, "stock": stock})
    return data

def parse_mercadolibre(html: str) -> list[dict]:
    soup = BeautifulSoup(html, "html.parser")
    items = soup.select("li.ui-search-layout__item")
    data = []
    for item in items:
        title_tag = item.select_one("h2.ui-search-item__title")
        price_tag = item.select_one("span.price-tag-fraction")
        if not title_tag or not price_tag:
            continue
        data.append({
            "title": title_tag.get_text(strip=True),
            "price": price_tag.get_text(strip=True),
        })
    return data

def parse_html(results: list[dict]) -> dict:
    """Recibe los HTMLs y devuelve un diccionario {site: DataFrame}"""
    site_data = {}

    for result in results:
        site = result["site"]
        html = result["html"]

        if site == "books":
            df = pd.DataFrame(parse_books(html))
        elif site == "mercadolibre":
            df = pd.DataFrame(parse_mercadolibre(html))
        else:
            logger.warning(f"No hay parser definido para el sitio '{site}'")
            continue

        if site not in site_data:
            site_data[site] = df
        else:
            site_data[site] = pd.concat([site_data[site], df], ignore_index=True)

    for site, df in site_data.items():
        logger.info(f"Datos parseados correctamente para {site}: {len(df)} filas")

    return site_data

