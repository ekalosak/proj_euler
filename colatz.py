def nxt(n):
    if n <= 0: raise ValueError("Can't handle non-natural values")
    elif n = 1: return 1
    else:
        if n % 2 == 0: return n/2
        else: return 3*n + 1

def seq(n):
    s = [n]
    while n != 1:
        n = nxt(n)
        s.append(n)
    return s

def test():
    assert nxt(3) == 10
    assert nxt(2) == 1
    assert nxt(1) == 1
    assert seq(3) == [3, 10, 5, 16, 8, 4, 2, 1]

if __name__ == '__main__':
    test()
