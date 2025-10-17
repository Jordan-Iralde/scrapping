import pandas as pd
import os
from core.logger import get_logger

logger = get_logger(__name__)

def save_to_csv(df: pd.DataFrame, path: str):
    """Guarda el DataFrame en formato CSV."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_csv(path, index=False, encoding="utf-8-sig")
    logger.info(f"Archivo guardado: {path}")
