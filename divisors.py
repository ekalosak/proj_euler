import pdb
from primes import just_exp

def num_divisors(n):
    ''' find the number of divisors (inc t) of t '''
    if n == 0: return 0
    je = just_exp(n)
    je = je[1:]
    if not je: return 1     # case n is 1
    if len(je) == 1: return 2   # case n is prime
    return reduce(lambda e1, e2: (e1 + 1)*(e2 + 1), je)

def test():
    assert num_divisors(7) == 2
    assert num_divisors(6) == 4
    assert num_divisors(100) == 9
    assert num_divisors(1) == 1
    print 'Passed tests!!'

if __name__ == '__main__':
    test()
