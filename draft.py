def fibonacci_rec(n):
    if n <= 2:
        return 1

    return fibonacci_rec(n - 1) + fibonacci_rec(n - 2)

print(fibonacci_rec(45))