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
from testing import benchmark

@benchmark
def main(N):
    # want the first triangle number with more than N divisors
    n = 1
    t = 1
    ndiv = 1
    while ndiv <= N:
        t = tri(n)
        n = n + 1
        ndiv = num_divisors(t) 
    return n, t, ndiv

def test():
    assert main(5) == 5, 28, 6
    print "Passed tests!!"

if __name__ == '__main__':
    test()
    main(500)
