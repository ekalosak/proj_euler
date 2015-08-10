##  import pdb

def tri_next(t, n):
    ''' given the n'th triangle number t, make the next one. '''
    return (t + n + 1, n + 1)

def tri(n):
    ''' find the n'th triange number '''
    t1 = 1
    n1 = 1
    while n1 < n:
        t1, n1 = tri_next(t1, n1)
    return t1

def tri_state(T):
    ''' given T list of first n=len(T) triangles, return list with next
    triangle'''
    n = len(T)
    if T:
        T.append(tri_next(T[-1], n)[0])
        return T
    else:
        return [1]

def first_n_tris(n):
    T = []
    for k in range(n):
        T = tri_state(T)
    return T

def test():
    assert tri(1) == 1
    assert map(lambda t: tri(t), range(1,6)) == [1, 3, 6, 10, 15]
    assert first_n_tris(6) == [1, 3, 6, 10, 15, 21]
    print 'Passed tests!!'
    
if __name__ == '__main__':
    test()
