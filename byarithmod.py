#!/usr/bin/env python3

# Crible d'eratosthene par Arithmetique modulaire

# fonction qui regarde si prod et cnt sont relativement premier (pas de diviseur commun)
def isrelatprime(prod, cnt):
    res = prod % cnt
    if res == 1:
        return True
    if res == 0:
        return False
    return isrelatprime(cnt, res)

def get_primes_list(maxval):
    # pour l'affichage
    plist = [2]
    # un seul produit sert comme aggrégat de tous les primes
    prod = 2
    cnt = 3
    while True:
        # si on est de proche en proche (sans trou) relativement prime on est prime
        if isrelatprime(prod, cnt):
            plist.append(cnt)
            prod *= cnt
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
