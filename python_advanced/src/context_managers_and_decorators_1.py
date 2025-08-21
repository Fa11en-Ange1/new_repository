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

#5
def retry(n):
    def decorator(func):
        def wrapper():
            for i in range(n):
                try:
                    return func()
                except Exception as e:
                    print("Error:", e)
            print("Failed to execute")
        return wrapper
    return decorator


@retry(3)
def unstable():
    print("Processing")
    raise ValueError("Error")

unstable()

#6
def memoize(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

@memoize
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print(factorial(5))
