# -*- coding: utf-8 -*-

'''
小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
低于18.5：过轻
18.5-25：正常
25-28：过重
28-32：肥胖
高于32：严重肥胖
'''

print('please input the height(m):')
height = float(input())
print('please input the weight(kg):')
weight = float(input())
bmi = weight / (height ** 2)

if bmi < 18.5:
    print('BMI指数是%.1f:过轻' % bmi)
elif 18.5 <= bmi < 25:
    print('BMI指数是%.1f:正常' % bmi)
elif 25 <= bmi < 28:
    print('BMI指数是%.1f:过重' % bmi)
elif 28 <= bmi < 32:
    print('BMI指数是%.1f:肥胖' % bmi)
elif 32 <= bmi:
    print('BMI指数是%.1f:严重肥胖' % bmi)