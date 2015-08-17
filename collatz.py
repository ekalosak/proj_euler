from tree import tree
from stack import stack
import pdb

def nxt(n):
    ''' return the next value in the Collatz sequence '''
    if n <= 0: raise ValueError("Can't handle non-natural values")
    elif n == 1: return 1
    else:
        if n % 2 == 0: return n/2
        else: return 3*n + 1

def prev(n):
    ''' go backwards in the Collatz sequence '''
    if n <= 0: raise ValueError("Can't handle non-natural values")
    if (n - 1) % 3 == 0:
        return [(n-1)/3, 2*n]
    else:
        return [2*n]
    
def seq(n):
    s = [n]
    while n != 1:
        n = nxt(n)
        s.append(n)
    return s

def maxlen1(N):

    ''' calculate collatz tree forward brutishly
    Initialize a list from 1..N
    Calculate for each t in T
    Once a number is encountered, add it to a dict with number
        and length of chain.
    When a number is encountered, add it to a stack
    Return (n, l) number and length of number with longest
        chain under or equal N (n <= N)'''

    if not type(N) == int:
        msg = "Value " + str(N) + " is not an integer"
        raise ValueError(msg)
    elif N <= 0:
        msg = "Value " + str(N) + " is not greater than 0"
        raise ValueError(msg)

    if N == 1:
        return (1, [1])
    elif N == 2:
        return (2, [2])

    R = {1: 1, 2: 2, 4: 3}  # records lengths of chain, avoid obv cycle
    T = range(N, 0, -1)

    for k in R:
        if k in T:
            T.remove(k) # remove the already calculated chain lengths

    while len(t) > 0:
        n = T.pop()
        inR = False
        while not inR:
            nx = nxt(n)
            # TODO

        if n in t:
            t.remove(n) # so we know when we've calculated lens for all nums
        s.push(prev(n)) # set up the previous elements in the seq

    mxL = max(r.values())
    mxN = [k for k in r if r[k] == mxL]
    return (mxL, mxN)

def maxlen2(N):

    ''' calculate collatz tree backwards brutishly
    Initialize a list from 1..N
    Calculate backwards from 1 -> 2 -> 4 -> (1,8) etc. 
    Once a number is encountered, add it to a dict with number
        and length of chain.
    When a number is encountered, add it to a stack
    Return (n, l) number and length of number with longest
        chain under or equal N (n <= N)'''

    if not type(N) == int:
        msg = "Value " + str(N) + " is not an integer"
        raise ValueError(msg)
    elif N <= 0:
        msg = "Value " + str(N) + " is not greater than 0"
        raise ValueError(msg)

    if N == 1:
        return (1, [1])
    elif N == 2:
        return (2, [2])

    r = {1: 1, 2: 2, 4: 3}  # records lengths of chain, avoid obv cycle
    s = stack([8])  # holds numbers to be computed
    t = range(1, N)

    for k in r:
        if k in t:
            t.remove(k) # remove the already calculated chain lengths

    while len(t) > 0:
        pdb.set_trace()
        n = s.pop() # get a number that has yet to have its len calcd
        nx = nxt(n) # check what its parent in the tree is
        r[n] = r[nx] + 1  # n's length is 1 + parent's length 

        if n in t:
            t.remove(n) # so we know when we've calculated lens for all nums
        s.push(prev(n)) # set up the previous elements in the seq

    mxL = max(r.values())
    mxN = [k for k in r if r[k] == mxL]
    return (mxL, mxN)

def test():
    assert nxt(3) == 10
    assert nxt(2) == 1
    assert nxt(1) == 1
    assert seq(3) == [3, 10, 5, 16, 8, 4, 2, 1]
    assert maxlen2(2) == (2, [2])
    assert maxlen2(10) == (9, len(seq(9)))
    print "Tests passed!!, maxlen1 not tested"

if __name__ == '__main__':
    test()
