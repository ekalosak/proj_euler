import pdb
import math

def div(n):
    # find the divisors of n
    r = []
    for k in range(1, int(n/2) + 1):
        if n % k == 0:
            r.append(k)
    r.append(n)
    return r

def num_div(n):
    r = 0
    if n > 1: r = r + 2 # 1 and n divide n
    elif n == 1: return(1)
    else: raise ValueError('Cannot find number of divisors of nonnatural number\
        %d' % n)
    sq = math.sqrt(n)
    for k in range(2, int(sq) + 1):
        if n % k == 0:
            if k == int(sq) and (int(sq) - sq == 0.0):
                r = r + 1
            else:
                r = r + 2
    return r

def test():
    for k in range(1, 50):
        assert len(div(k)) == num_div(k)
    print 'Passed tests!!'

if __name__ == '__main__':
    test()
