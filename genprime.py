def take(n, g):
    for _ in range(n):
        yield next(g)

def genprime():
    yield 2
    yield 3
    lsp = [2, 3]
    n = lsp[-1] + 2
    while True:
        if not any(filter(lambda _: n % _ == 0, lsp)):
            lsp.append(n)
            yield n
        n += 2
