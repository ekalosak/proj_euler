'''
Author: eric kalosa-kenyon 8-9-15
Problem: first triange to have over 500 divsors
'''

import math
import numpy as np

def tri(t, n):
    ''' given the n'th triangle number t, make the next one. '''
    m = n + 1
    return (t + m, m)

def divisors(t):
    ''' find the number of divisors (inc t) of t '''
    pfac = prime_factors(t)

    
def prime(upto=100):
    ''' http://rebrained.com/?p=458 '''
    return filter(lambda num: (num %
        np.arange(2,1+int(math.sqrt(num)))).all(), range(2,upto+1))

def prime_factors(n):
    pfac = []   # List of tuples (e, p) by FTA
    primes = prime(int(math.sqrt(n)))
    w = 0
    p = primes[w]
    while n >= p**2:
        e = 0
        while not n % p:
            e = e + 1
            n = n / p
        if e:
            pfac = pfac + [(e, p)]
        w = w + 1
        p = primes[w]
    if n > 1:
        pfac = pfac + [(1, n)]
    return pfac

def main():
    t = 1
    n = 1
    print prime_factors(100)

if __name__ == '__main__':
    main()
