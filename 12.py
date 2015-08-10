'''
Author: eric kalosa-kenyon 8-9-15
Problem: first triangle to have over 500 divsors
'''

# sys imports
import pdb
import time

# math imports
import math
import numpy as np

# local imports
from triangle import tri
from divisors import num_divisors

def benchmark(fxn):

    def w_bmk(*args, **kw):
        t0 = time.clock()
        r = fxn(*args, **kw)
        t1 = time.clock()
        print "Function took ", t1-t0, " seconds."
        return r

    return w_bmk

@benchmark
def main(N):
    # want the first triangle number with more than N divisors
    ndiv = 1
    n = 1
    ndivmax = 1
    while ndiv <= N:  # Until this loop reaches its goal
        t = tri(n)
        ndiv = num_divisors(t)
        if ndiv > ndivmax:
            ndivmax = ndiv
            print n, t, ndiv
        n = n + 1
    print t, ' has ', ndiv, ' divisors.'
    return t

def test():
    assert main(5) == 28
    print "Passed tests!!"


if __name__ == '__main__':
    test()
    main(500)
