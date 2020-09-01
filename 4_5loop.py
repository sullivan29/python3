# #!/usr/bin/env python3

'''if-else语句'''
# number = int(input('Enter a number: '))
# if number < 100:
#     print('the number is less than 100')
# else:
#     print('the number is greater than 100')

# 真值检测 if x: ; instead of in x == true:
# if expression:

'''while loop'''
# while condition:
#     statement
# n = 0
# while n < 11:
#     print(n)
#     n += 1

'''Fibonacci sequence'''
# a, b = 0, 1
# while b < 100:
#     print(b, end=' ') # 参数end替换
#     a, b = b, a+b

'''exponential function'''
# x = float(input('Enter the value of x: '))
# n = 1
# term = 1
# result = 1
# while n < 100:
#     term *= x / n  # note 随n的增加，term为n!，适用多项求积。
#     result += term  # 与上一行联动，适用多项求和时。
#     n += 1
#     if term < 0.0001:
#         break
# print('No of times= {} and Sum= {}'.format(n, result))

'''乘法表'''
# print('-'*50)
# i = 1
# while i < 11:
#     for n in range(1,11):
#         print('{:5d}'.format(i * n), end=' ')
#     print()
#     i += 1
# print('-'*50)


# print('-'*50)
# for i in range(1, 11):
#     for n in range(1, 11):
#         print('{:5d}'.format(i * n), end=' ')
#     print()
# print('-'*50)

'''列表生成式,array.reshape'''
# print('-'*50)
# import numpy as np
# l1 = [i * n for i in range(1,11) for n in range(1,11)]
# a = np.array(l1).reshape(10,10)
# print(a)

'''zip'''
# 接受可迭代对象(tuple,list,dict)作为参数，打包成tuple，返回由tuples组成的iterator.
# l1 = list('abcd')
# l2 = list('1234')
# print(list(zip(l1, l2)))

# str1 = 'abcd'
# str2 = '1234'
# print([i+n for i, n in zip(str1, str2)])

'''*用法'''
'''元组解包'''
# l3 = list('1234')
# a, b, *c = l3
# print(c)


# def fun(numbers):
#     sum = 0
#     for k in numbers:
#         sum += k
#     return sum

# lst = list((1,2,3,4))
# print(lst)
# print(fun(lst))

# def fun1(*numbers): # 函数定义收集参数
#     sum = 0
#     for k in numbers:
#         sum += k
#     return sum

# print(fun1(1,2,3,4))
# print(fun1(*lst)) # 函数调用时解包参数
# print(fun1(1,2,3))
# # compared with the above funciton,可变参数不是list/tuple

'''位置参数、默认参数、可变参数'''
# def power(x,n=2):
#     s = 1
#     assert isinstance(n, int) and n > 0
#     for k in range(0,n):
#         s *= x
#     return s 

# print(power(5,-2))
# # x 位置参数， n默认参数

print('X = {}, Y = {}'.format(*('a',2)))
