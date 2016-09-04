#!/usr/bin/env python3

# Crible d'eratosthene standard

def get_primes_list(maxval):
    # calcul une liste pleine de nombre
    ls = list(range(2, maxval))
    sz = len(ls)
    # parcours complet
    for idx in range(sz):
        # si non precedement nettoyé
        if ls[idx] != -1:
            for idx2 in range(idx + 1, sz):
                # j'enleve ce qui est divisible
                if ls[idx2] != -1 and (ls[idx2] % ls[idx]) == 0:
                    ls[idx2] = -1
    return list(filter(lambda x: x > 0, ls))

if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser(description="Compute primes")
    p.add_argument("maxval", type=int, help="Maximum value")
    arg = p.parse_args()
    print(repr(get_primes_list(arg.maxval)))
