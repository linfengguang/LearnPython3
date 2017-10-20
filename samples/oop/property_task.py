# -*- coding: utf-8 -*-

'''
请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution
'''

class Screen(object):

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise ValueError('width must be integer !')
        if value < 1 or value > 10:
            raise ValueError('width must between 1-10 !')
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise ValueError('height must be integer !')
        if value < 1 or value > 6:
            raise ValueError('height must between 1-6 !')
        self._height = value

    @property
    def resolution(self):
        return ('%s x %s' % (self._width, self._height))

if __name__ == '__main__':
    page = Screen()
    page.width = 10
    page.height = 6
    print('the page\'s width is: %scm\nthe page\'s heigth is: %scm\nthe page\'s resolution is: %s\n'
          % (page.width, page.height, page.resolution))
