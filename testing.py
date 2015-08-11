import time

def benchmark(fxn):

    def w_bmk(*args, **kw):
        t0 = time.clock()
        r = fxn(*args, **kw)
        t1 = time.clock()
        print "Function took ", t1-t0, " seconds."
        return r

    return w_bmk

