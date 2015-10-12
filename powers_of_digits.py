N = 10**7
p = 5

s = 0
i = 2

try:
    while True:
        a = str(i)
        b = 0
        for c in a:
            b = b + int(c)**p
        if b == i:
            print b
            s = s + b
        i += 1
        if i % 100000 == 0:
            print "tested ", i

except KeyboardInterrupt as ke:
    print "quit at ", i
    pass

print "sum is ", s
