# -*- coding: utf-8 -*-

class testself(object):

	# def __init__(self, arg):
	# 	super(ClassName, self).__init__()
	# 	self.arg = arg
	def printself():
		# print()
		print(__class__)

if __name__ == '__main__':
    
    test = testself()
    # test.printself()
    testself.printself()
    pass
