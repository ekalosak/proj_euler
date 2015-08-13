'''
Author: eric kalosa-kenyon 
Problem: 15 - find lattice paths in 20x20 grid
'''

import math as ma
import numpy as np
from scipy.misc import comb

''' finds the number of lattice paths in an NxM grid
how: have to go down N times, over M times, no backtracing
    so count the ways e.g. (o,d,d,o) N d's and M o's
    can be rearranged uniquely '''

''' Naievely, 1xN has N+1 solutions, so 2xN has, summed over all i = 0 to N,
(N-i)*(N - (N-i) + 1). Similarly, 3xN has, summed over all i = 0 to N, j = i
to N, ...? the previous formula seems suspect '''

''' Apparently we can do this with N+M choose M '''

def numPaths(N, M):
    ''' finds num paths in an NxM lattice without analytic formula '''
    return int(comb(N + M, M))

def main():
    ''' '''
    print numPaths(20, 20)

def test():
    assert numPaths(2, 2) == 6
    print "Passed tests!!"

if __name__ == '__main__':
    test()
    main()
