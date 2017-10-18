# -*- coding: utf-8 -*-

from collections import Iterable

L1 = ['Hello', 'World', 18, 'Apple', None]
for m in L1:
    if not isinstance(m, str):
        L1.pop(L1.index(m))
print([s.lower() for s in L1])