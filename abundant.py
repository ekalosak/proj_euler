'''
Find the sum of all the positive integers which cannot be written as the sum of
two abundant numbers.
Abundant number is num whose sum(divisors) > num
Those numbers > 28123 can be written as sums of abundant numbers

Breakdown:
    find all abundant numbers
    find all pos ints who cannot be written as sums of two abundant numbers
    find compliment of that set
    sum those numbers
'''

import pdb
import math
from divisors import div
import itertools as itt
import pickle
import os
import sys

FN = "./abundant_numbers.p"
MEM = "./abundant_memoization.p"

def abundant(n):
    # returns true if n is abundant
    assert type(n) == int
    assert n > 0
    ds = div(n)
    # print "the divisors of {} are {}".format(n, ds)
    sds = sum(ds[:-1])
    if sds > n:
        return True
    else:
        return False

def find_abundant(N):
    # returns a list of abundant numbers less than N

    sufficient = False
    if os.path.exists(FN):
        print "Loading abundant numbers"
        pa = pickle.load(open(FN, "rb"))
        if N <= pa[0]:
            print "There were sufficiently many in the previous calculation"
            abts = [a for a in pa[1] if a <= N]
        else:
            print "There were not enough in the previous calculation"
            abts = [k for k in range(1, N) if abundant(k)]
            pa = N, abts
            pickle.dump(pa, open(FN, "wb"))
    else:
        print "Calculating abundant numbers"
        abts = [k for k in range(1, N) if abundant(k)]
        pa = N, abts
        pickle.dump(pa, open(FN, "wb"))

    return abts

def reverse_self_iter(ns):
    k = 0
    while k < len(ns):
        j = k
        while j < len(ns) - k:
            try:
                yield ns[k], ns[-j]
            except IndexError as e:
                pdb.set_trace()
            j = j + 1
        k = k + 1

def is_sum_of_abundant(n, abdnts):
    # returns true if n = a + b where a and b are abundant
    qq = [q for q in abdnts if q <= n]
    # for a, b in itt.product(qq, qq):
    for a, b in reverse_self_iter(qq):
        if n == a + b:
            return a, b
    return 0, 0

def test():
    assert div(12) == [1, 2, 3, 4, 6, 12]
    assert abundant(12)
    abdnts = find_abundant(100)
    # print abdnts
    assert is_sum_of_abundant(24, abdnts)
    assert not abundant(11)
    # assert not is_sum_of_abundant(11, abdnts).all()
    print "Passed tests!!"

def main():
    N = 28124
    print "finding abundant numbers less than {}".format(N)
    abts = find_abundant(N)
    print "found {} abundant numbers".format(len(abts))
    # sabts = [k for k in range(1, N) if is_sum_of_abundant(k, abts)]
    print "finding numbers that are sums of abundant numbers"

    if os.path.exists(MEM):
        start, sabts, nsabts = pickle.load(open(MEM, "rb"))
    else:
        start = 0
        sabts = []
        nsabts = []

    try:
        for k in range(start, N):
            print "testing {}".format(k),
            a, b = is_sum_of_abundant(k, abts)
            if a or b:
                # print "{} is the sum of abundant numbers {} + {}".format(k, a, b)
                print "\tpassed: {} + {}".format(a, b)
                sabts.append(k)
            else:
                # print "{} is not the sum of abundant numbers".format(k)
                print "\tfailed"
                nsabts.append(k)

    except KeyboardInterrupt as ke:
        print "\npickling progress: {} at {}".format(k, MEM)
        pickle.dump([k, sabts, nsabts], open(MEM, "wb"))
        print "pickled!"
        sys.exit(1)

    print "The sum of all the positive integers that cannot",
    print " be written as the sum of two abundant numbers is {}".format(
            sum(nsabts))

if __name__ == '__main__':
    test()
    try:
        main()
    except Exception as ee:
        pdb.set_trace()
