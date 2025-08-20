#1.0
import time

class Timer:

    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        end = time.perf_counter()
        difference = end - self.start
        print(f'time has passed: {difference:.5f}')

with Timer():
    time.sleep(2)

#1.1
from contextlib import contextmanager
import time

@contextmanager
def my_context():
    start = time.perf_counter()
    yield
    end = time.perf_counter()
    print(f'time has passed: {end - start:.5f}')

with my_context():
    time.sleep(2)  # цей код заміряється


#2.0
class DividerContext:

    def __init__(self, symbol):
        self.symbol = symbol

    def __enter__(self):
        print(self.symbol, end=' ')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(self.symbol)


with DividerContext('*'):
    print('text is needed here', end=' ')

#2.1
from contextlib import contextmanager

@contextmanager
def divider_context(symbol):
    print(symbol, end=' ')
    yield
    print(symbol)

with divider_context("*"):
    print("text is needed here", end=' ')

#3
def log_func(function):
    def wrapper():
        print('before the start')
        function()
        print('after the end')
    return wrapper()

@log_func
def in_progress():
    print('in progress')

