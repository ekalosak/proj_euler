def nxt(n):
    if n <= 0: raise ValueError("Can't handle non-natural values")
    elif n == 1: return 1
    else:
        if n % 2 == 0: return n/2
        else: return 3*n + 1

def seq(n):
    s = [n]
    while n != 1:
        n = nxt(n)
        s.append(n)
    return s

def maxlen1(N):
    r = {}  # r[n] = nxt(n)
    e = {}  # e[n] = len(seq(n))
    ''' for each n < N,
            calculate the collatz seq moving fwd from that
                record the next number and leave a space for len
            when established len sequence is reached, backpropogate lengths
    '''
    for n in range(1, N):
        u = []
        if n in r: continue
        else:
            pass    #TODO
    return r

def maxlen2(N):
    r = {}
    ''' calculate collatz tree backwards build same kind of structure as ml1
    above '''
    n = 1

def test():
    assert nxt(3) == 10
    assert nxt(2) == 1
    assert nxt(1) == 1
    assert seq(3) == [3, 10, 5, 16, 8, 4, 2, 1]
    print "Tests passed!!"

if __name__ == '__main__':
    test()
