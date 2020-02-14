def take(n, gen):
    res = []
    for _ in range(n):
        res.append(next(gen))
    return res

def prime_gen():
    yield 2
    yield 3
    prime_set = [2, 3]
    current_number = 5
    while True:
        if all(map(lambda _: current_number % _ != 0, prime_set)):
            yield current_number
            prime_set.append(current_number)
        current_number += 2
    
