import time
import functools
from unittest import mock


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

def patch_io(test_input_name):
    def decorator_patch_io(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            with mock.patch("decorators.open", mock.mock_open(read_data=kwargs[test_input_name])) as mock_file:
                return func(*args, **kwargs)
        return wrapper
    return decorator_patch_io
        