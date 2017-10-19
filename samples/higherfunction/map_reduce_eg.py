# -*- coding: utf-8 -*-

from functools import reduce

'''
f(x) = x^2
'''

def f(x):
    return x * x
print(list(map(f, range(1,10))))

def add(x, y):
    return x + y
print(reduce(add, (x for x in range(1, 10) if x % 2 != 0)))

def str2int(s):

    def fn(x, y):
        return x * 10 + y

    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

    return reduce(fn, map(char2num, s))

print(str2int('13579'))
