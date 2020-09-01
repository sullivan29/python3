# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
'''!/usr/bin/env python3'''
def palindrome(s):
    return s == s[::-1]

if __name__ == '__main__':
    s = input('Enter a string: ')
    if palindrome(s):
        print('yay a palindrome')
    else:
        print('oh, no')


# %%
'''全局/局域变量'''
def change():
    a = 90
    print(a)

a = 9
print('before the function call', a)
print('inside change function', end=' ')
change()
print('after the function call', a)
# 不同的a, 函数内部局域变量

# b = 7
# def chan():
#     print(b)
# chan()

# c = 5
# def ch():
#     print(c)
#     c = 10
#      # c作为局部变量，在print后定义, raise Error
# print('before the function call', c)
# print('inside change function', end=' ')
# ch()
# print('after the function call', c)


# %%
'''global'''
d = 7
def change2():
    global d # 声明全局变量，函数内均为全局变量
    print(d)
    d = 100
print('before the function call', d)
print('inside change function', end=' ')
change2()
print('after the function call', d)


# %%
'''默认参数'''
# 默认参数指向不变对象，&其后不能有普通参数

def test(a, b=9): # a, b 均为位置参数positional argument
    if a > b:
        return  True
    else:
        return False

test(22)

'''关键字参数'''
#扩展函数的功能

def func(a, b=5, **kw):
    print('a is', a, 'and b is', b, 'and other is', kw)

func(7, c=10, d= 'city')
# c=10 关键字赋值 keyword = value

'''强制关键字'''
# *特殊分隔符，其后为关键字
# call 必须传入参数名

# def hello(*, name='user', age=18 ):
#     print('hello', name, 'your age is {}'.format(age) )

# hello(name='Frank', )




# %%
'''文档字符串'''
#交互模式，说明文档
import math

def longest_side(a, b):
    '''
    Function to find the length ...

    :arg a: side a of the triangle

    :return: length of the longest side'''
    return math.sqrt(a*a + b*b)

if __name__ == '__main__':
    print(longest_side.__doc__)
    print(longest_side(3, 4))


# %%
'''高阶函数'''

def high(l):
    return [i.upper() for i in l]

#返回列表 
l1 = ['python', 'linux']
high(l1)

def test(h, l): # h 函数可作为pisitional argument
    return h(l)

test(high,l)


# %%
l = []
for i in l1:
    l.append(i.upper())
l

s = set()
for i in l1:
    s.add(i.title())

def titl(l):
    return set([i.title() for i in l])

#返回集合
titl(l)


# %%
'''map'''

l2 = list(range(1,6))
def square(num):
    return num * num

set(map(square,l2))


