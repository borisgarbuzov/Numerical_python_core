#!/usr/bin/python
## example4_5


from ridder import *

def f(x):
    a = (x - 0.3)**2 + 0.01
    b = (x - 0.8)**2 + 0.04
    return 1.0/a - 1.0/b


print("root =",ridder(f,0.0,1.0))
input("Press return to exit")