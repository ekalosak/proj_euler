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
from divisors import num_div
from testing import benchmark

@benchmark
def main(N):
    # want the first triangle number with more than N divisors
    n = 1
    ndiv = 1
    while ndiv <= N:
        t = tri(n)
        ndiv = num_div(t)
        n = n + 1
    return n - 1, t, ndiv

def test():
    assert main(5) == (7, 28, 6)    # case given in problem
    assert main(1) == (2, 3, 2)
    print "Passed tests!!"

if __name__ == '__main__':
    test()
    N = 500
    n, t, d = main(N)
    print "First traingle number with more than ", N, " divisors is ",\
        t, ' with ', d, ' divisors.'
