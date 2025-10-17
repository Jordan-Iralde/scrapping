import os
from core.logger import get_logger

logger = get_logger(__name__)

def save_to_csv_by_site(data_dict: dict, folder="data/processed"):
    """Guarda cada DataFrame en un CSV separado por sitio"""
    os.makedirs(folder, exist_ok=True)
    for site, df in data_dict.items():
        path = os.path.join(folder, f"{site}.csv")
        df.to_csv(path, index=False, encoding="utf-8-sig")
        logger.info(f"Archivo guardado: {path}")
