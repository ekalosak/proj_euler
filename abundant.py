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
    return [k for k in range(1, N) if abundant(k)]

def is_sum_of_abundant(n, abdnts):
    # returns true if n = a + b where a and b are abundant
    qq = [q for q in abdnts if q <= n]
    ww = [w for w in abdnts if w <= n/2]
    ee = [e for e in abdnts[::-1] if e > n/2]
    # for a, b in itt.product(qq, qq):
    for a, b in itt.product(ww, ee):
        # print "is {} + {} == {}?".format(a, b, n),
        if n == a + b:
            # print "\tYes!"
            return a, b
        # else:
            # print "\tNo."

    for a, b in itt.product(qq, qq):
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
    sabts = []
    nsabts = []
    for k in range(1, N):
        print "testing {}".format(k),
        a, b = is_sum_of_abundant(k, abts)
        if a or b:
            # print "{} is the sum of abundant numbers {} + {}".format(k, a, b)
            print "\tpassed"
            sabts.append(k)
        else:
            # print "{} is not the sum of abundant numbers".format(k)
            print "\tfailed"
            nsabts.append(k)

    print "The sum of all the positive integers that cannot",
    print " be written as the sum of two abundant numbers is {}".format(
            sum(nsabts))

if __name__ == '__main__':
    test()
    main()
