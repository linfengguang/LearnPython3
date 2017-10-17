# -*- coding: utf-8 -*-

import math

'''
请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：
ax2 + bx + c = 0
的两个解
'''

def quadratic(a, b, c):
    if a == 0:
        print('系数不能为零!')
        return
    else:
        x1 = (-b + math.sqrt(abs(b ** 2 - 4*a*c))) / (2 * a)
        x2 = (-b - math.sqrt(abs(b ** 2 - 4*a*c))) / (2 * a)
        return x1,x2

print(quadratic(2, 3, 1))