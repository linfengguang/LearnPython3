# -*- coding: utf-8 -*-

# class Student(object):
#
#     def get_core(self):
#         return self._score
#
#     def set_score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an integer !')
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0-100 !')
#         self._score = value
#
# if __name__ == '__main__':
#
#     lisa = Student()
#     lisa.set_score(95)
#     print(lisa.get_core())
#     lisa.set_score(98)
#     print(lisa.get_core())
#

# class Student(object):
#
#     @property
#     def score(self):
#         return self._score
#
#     @score.setter
#     def score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an integer !')
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0-100 !')
#         self._score = value
#
# if __name__ == '__main__':
#
#     lisa = Student()
#     lisa.score = 80
#     print(lisa.score)
#     lisa.score = 988
#     print(lisa.score)

class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer !')
        if value < 0 or value > 100:
            raise ValueError('score must between 0-100 !')
        self._score = value

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        if not isinstance(value, int):
            raise ValueError('birth must be an integer !')
        if value < 1900 or value > 2017:
            raise ValueError('birth must between 1900-2017 !')
        self._birth = value

    @property
    def age(self):
        return 2017 - self._birth

if __name__ == '__main__':

    lisa = Student()
    lisa.score = 80
    print('lisa\'s score: %s' % lisa.score)
    lisa.birth = 1988
    print('lisa\'s age: %s' % lisa.age)