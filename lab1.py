############################################################
# Name: James Barbi
# Pledge: I pledge my Honor that I have abided by the Stevens Honor System.
# CS115 Lab 1
#
############################################################

import math
from functools import reduce

def add(x, y):
    return (x + y)

def inverse(n):
    return float(1 / n)

def e(n):
    l = range(1, n + 1)
    l = list(map(math.factorial, l))
    l = list(map(inverse, l))
    answer = reduce(add, l)
    return 1 + answer

print(inverse(4))
print(e(2))
print(e(3))
print(e(10))