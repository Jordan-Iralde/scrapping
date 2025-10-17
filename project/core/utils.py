import time
from functools import wraps
from core.logger import get_logger

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
