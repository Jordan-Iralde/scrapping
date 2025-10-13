import time
import random
import functools

def retry(max_retries=3, delay=2, backoff=2):
    """Decorador de reintento exponencial."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            retries = 0
            current_delay = delay
            while retries < max_retries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    retries += 1
                    if retries == max_retries:
                        raise
                    print(f"[Retry] Error: {e}, reintentando en {current_delay}s...")
                    time.sleep(current_delay)
                    current_delay *= backoff
        return wrapper
    return decorator

def random_delay(min_sec, max_sec):
    """Espera aleatoriamente entre min_sec y max_sec segundos."""
    time.sleep(random.uniform(min_sec, max_sec))
