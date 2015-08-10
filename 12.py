'''
Author: eric kalosa-kenyon 8-9-15
Problem: first triangle to have over 500 divsors
'''

# sys imports
import pdb

# math imports
import math
import numpy as np

# local imports
from triangle import tri_state
from divisors import num_divisors

def main(N):
    # want the first triangle number with more than N divisors
    T = []
    ndiv = 1
    n = 0
    ndivmax = 1
    while ndiv <= N:  # Until this loop reaches its goal
        T = tri_state(T)
        t = T[-1]
        ndiv = num_divisors(t)
        n = n + 1
        if ndiv > ndivmax:
            ndivmax = ndiv
            print n, t, ndiv
    print t, ' has ', ndiv, ' divisors.'
    return t

def test():
    assert main(5) == 28
    print "Passed tests!!"

if __name__ == '__main__':
    test()
    main(500)
