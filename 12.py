'''
Author: eric kalosa-kenyon 8-9-15
Problem: first triangle to have over 500 divsors
'''

import pdb

import math
import numpy as np
import functools as ft

def tri_next(t, n):
    ''' given the n'th triangle number t, make the next one. '''
    return (t + n + 1, n + 1)

def tri(n):
    ''' find the n'th triange number '''
    t1 = 1
    n1 = 1
    while n1 < n:
        t1, n1 = tri_next(t1, n1)
    return t1

def prime(upto=100):
    ''' http://rebrained.com/?p=458 '''
    return [1] + filter(lambda num: (num %
        np.arange(2,1+int(math.sqrt(num)))).all(), range(2,upto+1))

'''
def prime_factors(n):
    pfac = []   # List of tuples (e, p) by FTA
    primes = prime(int(math.sqrt(n)) + 1)
    w = 0
    p = primes[w]
    while n >= p**2:
        e = 0
        while not n % p:    # while n still divides p
            e = e + 1
            n = n / p
        if e:
            pfac = pfac + [(e, p)]
        w = w + 1
        p = primes[w]
    if n > 1:
        pfac = pfac + [(1, n)]
    return pfac
'''

def prime_factors(n):
    # not including 1
    pfac = []   # List of tuples (e, p) by FTA
    primes = prime(int(math.sqrt(n)) + 1)
    for p in primes:
        if p == 1: continue
        e = 0
        while not n % p:    # while n still divides p
            e = e + 1
            n = n / p   # chop away at the prime factorization
        if e:
            pfac = pfac + [(e, p)]
    if n > primes[-1]: pfac = pfac + [(1,n)]    # if n was prime to begin with
    return pfac

def just_exp(pfac):
    ''' given the list of prime factor exponent pairs [(e, p)..], return [e..]
    '''
    return map(lambda pe: pe[0], pfac)

def num_divisors(t):
    ''' find the number of divisors (inc t) of t '''
    pf = prime_factors(t)
    je = just_exp(pf)
    if len(je) == 1:
        return je[0][0] + 1
    return reduce(lambda e1, e2: (e1 + 1)*(e2 + 1), je)

def tests():
    assert prime(10) == [1, 2, 3, 5, 7]
    assert tri(4) == 10
    assert (2,2) in prime_factors(20) and (1,5) in prime_factors(20)
    assert num_divisors(20) == 6    # |{1, 2, 4, 5, 10, and 20}| = 6
    print prime_factors(3), just_exp(prime_factors(3)), num_divisors(3)
    pdb.set_trace()
    print "Passed tests!!"

def main():
    tests()
    t = 1   # the triangle number t is 1 for n = 1
    n = 1
    N = 500 # want the first triangle number with more than 500 divisors
    nfac = 1    # 1 has 1 divisor, base case
    print n, t, nfac
    while nfac <= 500:  # Until this loop reaches its goal
        t, n = tri_next(t, n)   #   get the next triange number
        nfac = num_divisors(t)
        print n, t, nfac
    print t, ' has ', nfac, ' divisors.'

if __name__ == '__main__':
    main()
