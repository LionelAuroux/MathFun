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
    plist = [2, 3]
    # un seul produit sert comme aggrégat de tous les primes
    prod = 2 * 3
    cnt = 5
    while True:
        # si on est de proche en proche (sans trou) relativement prime on est prime
        if cnt > maxval:
            break
        if isrelatprime(prod, cnt):
            plist.append(cnt)
            prod *= cnt
        cnt += 2
    return plist

### unit test
import unittest
from requests_html import HTMLSession

class Test(unittest.TestCase):
    def test_00(self):
        s = HTMLSession()
        r = s.get('https://primes.utm.edu/lists/small/10000.txt', verify=False)
        lines = list(map(lambda _: int(_), r.text.split()[15:-1]))
        print("%d is the last of %d first primes" % (lines[-1], len(lines)))
        p2 = get_primes_list(lines[-1])
        self.assertEqual(len(lines), len(p2))
        self.assertEqual(lines, p2)
        print("Algo OK")
###

if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser(description="Compute primes")
    p.add_argument("maxval", type=int, help="Maximum value")
    arg = p.parse_args()
    print(repr(get_primes_list(arg.maxval)))
