'''
Author: eric kalosa-kenyon 
Problem: find number under 1m that has longest collatz chain
How?
1. Dictionary of value that points to tuple of next val in chain and the lenght
    {k : (j, l)}
2. Compute the sequence backwards?
3. 
'''

import math as ma
import numpy as np
from testing import benchmark

@benchmark
def main():
    ''' Find the number under 100 mil with the longest collatz seq '''
    N = 10**8
    print collatz.maxlen1(N)

if __name__ == '__main__':
    main()
