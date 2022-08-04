def fibonacci(n):
    return 1 if n in [0, 1] else fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(int(input())))
