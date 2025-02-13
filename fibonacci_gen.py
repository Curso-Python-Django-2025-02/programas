def fibonacci(limit):
    a = 0
    b = 1
    while a < limit:
        c = a + b
        yield a
        a, b = b, c


g = fibonacci(1000)

for x in g:
    print(x)
