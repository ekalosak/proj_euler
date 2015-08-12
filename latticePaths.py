'''
Author: eric kalosa-kenyon 
Problem: 15 - find lattice paths in 20x20 grid
'''

import math as ma
import numpy as np

def numPaths(N, M):
    ''' finds the number of lattice paths in an NxM grid
    how: have to go down N times, over M times, no backtracing
        so count the ways e.g. (o,d,d,o) N d's and M o's
        can be rearranged uniquely '''

    ''' Naievely, 1xN has N+1 solutions, so 2xN has, summed over all i = 0 to N,
    (N-i)*(N - (N-i) + 1). Similarly, 3xN has, summed over all i = 0 to N, j = i
    to N, ...? the previous formula seems suspect '''

def main():
    ''' '''

def test():
    assert numPaths(2, 2) == 6
    print "Passed tests!!"

if __name__ == '__main__':
    test()
    main()
