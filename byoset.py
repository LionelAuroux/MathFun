#!/usr/bin/env python3

# Crible d'eratosthene par Ordered Set

def get_primes_list(maxval):
    # on a besoin d'une liste finale et pour le parcours iteratif
    plist = [2]
    # pour une recherche plus rapide
    pset = {2}
    cnt = 3
    while True:
        nd = 0
        # on test tous les precedents primes
        for it in plist:
            if cnt % it == 0:
                nd += 1
        # si c'est pas dedans c'est une prime
        if nd == 0 and cnt not in pset:
            plist.append(cnt)
            pset ^= {cnt}
        if cnt >= maxval:
            break
        cnt += 1
    return plist

if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser(description="Compute primes")
    p.add_argument("maxval", type=int, help="Maximum value")
    arg = p.parse_args()
    print(repr(get_primes_list(arg.maxval)))
