# -*- coding: utf-8 -*-

class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return print('%s: %s' % (self.name, 'A'))
        if 90 > self.score >= 60:
            return print('%s: %s' % (self.name, 'B'))
        else:
            return print('%s: %s' % (self.name, 'C'))

if __name__ == '__main__':
    bart = Student('bart', 60)
    lisa = Student('lisa', 80)
    bart.print_score()
    bart.get_grade()
