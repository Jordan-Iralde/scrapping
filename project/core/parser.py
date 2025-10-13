from bs4 import BeautifulSoup

def parse_items(html):
    """Extrae títulos, precios y URLs de productos desde una página HTML."""
    soup = BeautifulSoup(html, "html.parser")
    items = []

    for card in soup.select("li.ui-search-layout__item"):
        try:
            title = card.select_one("h2.ui-search-item__title").get_text(strip=True)
            link = card.select_one("a.ui-search-link")["href"]
            price = card.select_one(".price-tag-fraction").get_text(strip=True)
            items.append({
                "title": title,
                "url": link,
                "price": price
            })
        except AttributeError:
            continue

    return items
