class stack:

    def __init__(self, vals = []):
        self.c = vals

    def pop(self):
        return self.c.pop()
    def push(self, a):
        if type(a) == type([]):
            self.c = a + self.c
        else:
            self.c = [a] + self.c
    def vals(self):
        return self.c

    def __str__(self):
        return str(self.c)

def test():
    s = stack(range(3))
    assert s.pop() == 2
    assert s.vals() == [0, 1]
    s.push(1)
    assert s.vals() == [1, 0, 1]
    s.push([4, 5])
    assert s.vals() == [4, 5, 1, 0, 1]
    print "Passed tests!!"

if __name__ == '__main__':
    test()
