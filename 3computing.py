# #! /usr/bin/env python3
14 % 3
14 // 3

'''整数运算符'''
# days = int(input('enter days:'))
# months = days // 30
# days = days % 30
# print('Months = {}, Days = {}'.format(months, days))

# print('Months = {}, Days = {}'.format(*divmod(days, 30)))
# *拆封元组，函数调用解包参数

'''关系运算符'''
3 != 9

'''逻辑运算符'''
# 逻辑运算符优先级低于关系运算符
1 >= 0 and 4 < 6
# not 优先级最高

'''简写运算符'''
# N = 100
# a = 2
# while a < N:
#     print(str(a))
#     a *= a
#     # notice a*a, instead of a*2

'''类型转换'''
# float(string); int(string); str(float/integer)

'''program example'''
'''sum of 1/x'''
# sum = 0
# for i in range(1, 11):
#     sum += 1.0 / i
#     print('{:1d} | {:6.4f}'.format(i, sum))

'''quadratic equation'''
# import math
# a = int(input('Enter value of a: '))
# b = int(input('Enter value of b: '))
# c = int(input('Enter value of c: '))
# d = b * b - 4 * a *c
# if d < 0:
#     print('Roots are imaginary')
# else:
#     root1 = (-b + math.sqrt(d)) / (2 * a)
#     root2 = (-b - math.sqrt(d)) / (2 * a)
#     print('root 1 = ', root1)
#     print('root 2 = ', root2)

'''format函数'''
# test = 266438.3519
# print('tt   = {:,%}'.format(test))
print('Hello, {0}, I\'m {1}. My name is {0}'.format('Andrew', 'Berry'))  # 位置填充
print('Hello, {name1}, I\'m {name2}. My name is {name1}'.format(name1 = 'Andrew', name2 = 'Berry')) # key 填充

'''salesman salary'''
# basic_salary = 1500
# bonus_rate = 200
# commission_rate = 0.02
# n = int(input('Enter the number of inputs sold: '))
# price = float(input('Enter the camera price: '))
# bonus = n * bonus_rate  # 每个可能的变量单独列出，备用
# commission = n * price * commission_rate
# salary = basic_salary + bonus + commission
# # print('Bonus        = {:6.2f}'.format(bonus))
# # print('Commission   = {:6.2f}'.format(commission))
# # print('Gross salary = {:6.2f}'.format(salary))
# print('Bonus = {:6.2f} | Commission = {:6.2f} | Gross salary = {:6.2f}'.format(bonus, commission, salary))

'''Area of circle'''
import math
area = math.pi * (2 ** 2)
print('The area of circle is {:.10f}'.format(area))