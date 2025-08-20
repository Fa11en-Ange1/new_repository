#4
import time

def timeit(func):
    def wrapper():
        start_time = time.time()
        result = func()
        end_time = time.time()
        print(f"Execution time: {func.__name__}: {end_time - start_time} секунд")
        return result
    return wrapper

@timeit
def func_test():
    time.sleep(2)
func_test()