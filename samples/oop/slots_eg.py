# -*- coding: utf-8 -*-

from types import MethodType

class Student(object):
    __slots__ = ('name', 'age',)
    pass

class GraduteStudent(Student):
    pass

def set_age(self, age):
    self.age = age

if __name__ == '__main__':
    # Student.set_age = set_age
    lisa = Student()
    sam = GraduteStudent()
    lisa.name = 'lisa'
    print(lisa.name)
    # lisa.score = 99
    sam.score = 98
    # lisa.set_age(20)
    # print(lisa.age)
    # sam.set_age(22)
    # print(sam.age)










