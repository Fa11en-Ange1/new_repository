#1
def even_odd_generator(n):
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            yield "FizzBuzz"
        elif i % 3 == 0:
            yield "Fizz"
        elif i % 5 == 0:
            yield "Buzz"
        else:
            yield str(i)


for text in even_odd_generator(15):
    print(text)


#2
def fibonacci_generator(n):
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b


fib_gen = fibonacci_generator(50)
for i in range(10):
    print(next(fib_gen))