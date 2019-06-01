import time
import functools

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        output = func()
        end = time.perf_counter()
        print(f'{func.__name__} ran in {end - start} seconds')
        return output
    return wrapper

def fileio(file_path):
    def decorator_fileio(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            with open(file_path) as f:
                return func(f, *args, **kwargs)
        return wrapper
    return decorator_fileio
        