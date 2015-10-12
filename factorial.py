def factorial(N):
    if N == 1:
        return 1
    else:
        return N * factorial(N-1)

def tests():
    assert factorial(10) == 3628800
    print "passed tests!!"

def main():
    m = factorial(100)
    s = str(m)
    a = 0
    for k in s:
        a = a + int(k)
    print "Sum of digits in 100! is {}".format(a)

if __name__ == '__main__':
    tests()
    main()
