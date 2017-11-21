# -*- coding: utf-8 -*-

class desc(object):
	def __get__(self, ins, cls):
		print('self in desc: %s' % self)
		print(self, ins, cls)

class test(object):
	x = desc()
	def prt(self):
		print('self in test: %s' % self)

if __name__ == '__main__':
    test = test()
    test.prt()
    test.x

