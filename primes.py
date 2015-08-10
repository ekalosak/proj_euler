# import pdb

import math
import numpy as np

def prime(upto=100):
    ''' http://rebrained.com/?p=458 '''
    return [1] + filter(lambda num: (num %
        np.arange(2,1+int(math.sqrt(num)))).all(), range(2,upto+1))

def prime_factors(n):
    pfac = [(1, 1)]   # List of tuples (p, e) by FTA
    primes = prime(int(math.sqrt(n)) + 1)
    for p in primes:
        if p == 1: continue
        e = 0
        while not n % p:    # while n still divides p
            e = e + 1
            n = n / p   # chop away at the prime factorization
        if e:
            pfac = pfac + [(p, e)]
    if n > primes[-1]: pfac = pfac + [(n, 1)]    # if n was prime to begin with
    return pfac

def _just_exp(pfac):
    ''' given the list of prime factor exponent pairs [(e, p)..], return [e..]
    '''
    return map(lambda pe: pe[1], pfac)

def _just_fac(pfac):
    return map(lambda pe: pe[0], pfac)

def just_exp(n):
    return _just_exp(prime_factors(n))

def just_fac(n):
    return _just_fac(prime_factors(n))

def test():
    assert prime(10) == [1, 2, 3, 5, 7]
    assert just_fac(10) == [1, 2, 5]
    assert just_fac(20) == [1, 2, 5]
    assert just_fac(7) == [1, 7]
    assert just_exp(7) == [1, 1]
    assert just_fac(100) == [1, 2, 5]
    assert just_exp(100) == [1, 2, 2]
    print "Passed tests!!"

if __name__ == '__main__':
    test()
