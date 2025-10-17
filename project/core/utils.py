import time
import os
from functools import wraps
from core.logger import get_logger
import yaml

logger = get_logger(__name__)

def retry(retries=3, delay=1):
    """Decorador para reintentar funciones que pueden fallar (como requests)."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    logger.warning(f"Intento {i+1}/{retries} falló: {e}")
                    time.sleep(delay)
            raise Exception(f"{func.__name__} falló después de {retries} intentos.")
        return wrapper
    return decorator

def load_config(filename="config.yaml"):
    """Carga la configuración desde el archivo YAML."""
    # Obtener la ruta absoluta del directorio del script principal
    base_dir = os.path.dirname(os.path.abspath(__file__))  # core/
    project_dir = os.path.abspath(os.path.join(base_dir, ".."))  # ../
    path = os.path.join(project_dir, filename)
    
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)