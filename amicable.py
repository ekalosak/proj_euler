'''
Author: eric kalosa-kenyon 
Problem: 21, find sum of amicabel nums < 10000

Plan1:
    rs = range(1,N)
    amic = []
    for r in rs:
        a = amicable(r) returns amica-pair of r if exists, othw 0
        if a:
            amic.append((r, a)) record the amicable pair
            rs.remove(a) and make sure we don't recalculate that amicable
    return amic
'''

import math as ma
import numpy as np
import pdb

def divisors(N):
    divs = []
    for n in range(1, N):
        if N % n == 0:
            divs.append(n)
    divs.append(N)
    return divs

def amicable(N):
    ''' return amicable pair of r, othw 0
    1. find proper divisors of r
    2. sum those =: a
    3. find proper divisors of a
    4. sum those ?= r
    '''
    divs = divisors(N)
    divs.remove(N)
    poss_am = sum(divs)
    a_divs = divisors(poss_am)
    a_divs.remove(poss_am)
    if sum(a_divs) == N:
        return poss_am
    else:
        return 0

def find_amicables(N):
    ''' return a list of amicable numbers between 1 and N '''
    amicables = []
    for n in range(N + 1):
        a = amicable(n) 
        if a and a != n and a not in amicables and n not in amicables:
            print a, n
            amicables.append(a)
            amicables.append(n)
    return amicables

def main():
    ''' '''
    N = 10000
    amic = find_amicables(N)
    s = sum(amic)
    msg = "The first %d amicable numbers sum to %s" % (N, s)
    print msg

def test():
    assert divisors(6) == [1, 2, 3, 6]
    assert amicable(220) == 284
    assert not amicable(50)
    fa = find_amicables(250)
    assert all([x in fa for x in [220, 284]]) and len(fa) == 2
    print "Passed tests!!"

if __name__ == '__main__':
    test()
    main()
