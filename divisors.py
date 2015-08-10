import pdb
import math

def div(n):
    r = []
    for k in range(1, int(n/2) + 1):
        if n % k == 0:
            r.append(k)
    r.append(n)
    return r

def num_div(n):
    r = 1
    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            if k == int(math.sqrt(n)):
                r = r + 1
            else:
                r = r + 2
    if n > 1: r = r + 1
    return r

def test():
    for k in range(1, 50):
        assert len(div(k)) == num_div(k):
    print 'Passed tests!!'

if __name__ == '__main__':
    test()
