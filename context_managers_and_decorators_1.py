#4
from contextlib import contextmanager
import time

@contextmanager
def timeit():
    start_time = time.time()
    yield
    end_time =  time.time()
    print(f'Execution time: {end_time - start_time: }')


