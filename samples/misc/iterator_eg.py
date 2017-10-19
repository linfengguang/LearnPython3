# -*- coding: utf-8 -*-

from collections import Iterable,Iterator

print('list is Iterable:', isinstance([], Iterable))
print('dict is Iterable:', isinstance({}, Iterable))
print('int is Iterable:', isinstance(123, Iterable))

print('list is Iterator:', isinstance([], Iterator))
print('iter(list) is Iterator:', isinstance(iter([]), Iterator))
print('(x for x in range(10)) is Iterator:', isinstance((x for x in range(10)), Iterator))


