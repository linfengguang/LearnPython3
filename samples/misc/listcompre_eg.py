# -*- coding: utf-8 -*-

print([x * x for x in range(1,11)])
print([x * x for x in range(1,11) if x % 2 == 0])
print([m + n for m in 'ABC' for n in 'abc'])

L = ['Hello', 'World']
print([s.lower() for s in L])