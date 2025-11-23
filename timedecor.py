import functools
import time 
def timedecor(func):
    functools.wraps(func)
    async def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = await func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Время выполнения: {end - start:.6f} секунд")
        return result
    return wrapper
