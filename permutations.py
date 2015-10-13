'''
find the millionth lexographical permutation of 0..9
'''

import os, sys, pdb, math

def lex_permute(ls):
    pass

def tests():
    assert lex_permute("0123") == "0132"
    print "passed tests!!"

def main():
    pass

if __name__ == "__main__":
    tests()
    try:
        main()
    except KeyboardInterrupt as ke:
        pdb.set_trace()
