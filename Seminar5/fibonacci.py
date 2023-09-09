def gen_fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fib = gen_fib()
for _ in range(10):
    print(next(fib))
