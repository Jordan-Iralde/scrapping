from bs4 import BeautifulSoup
import pandas as pd
from core.logger import get_logger

logger = get_logger(__name__)

def parse_html(html_pages: list[str]) -> pd.DataFrame:
    """Procesa las páginas HTML y devuelve un DataFrame con los datos extraídos."""
    data = []

    for html in html_pages:
        soup = BeautifulSoup(html, "html.parser")
        items = soup.select("div.item")  # ejemplo: cambia según tu web

        for item in items:
            name = item.select_one(".title").get_text(strip=True) if item.select_one(".title") else "N/A"
            price = item.select_one(".price").get_text(strip=True) if item.select_one(".price") else "N/A"

            data.append({
                "name": name,
                "price": price,
            })

    df = pd.DataFrame(data)
    logger.info(f"Datos parseados correctamente: {len(df)} filas")
    return df
