# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# 数据结构:数据储存、组织的方式
a = [23, 45, 1, -3434, 234]
a.append(45)
# print(a)

'''插入元素insert'''
a.insert(0,1)
print(a)
a.insert(-1,45)
print(a)

'extend'
b = [56,0]
a.extend(b)

'''count'''
print(a.count(45))

str1 = 'hello'
str1.count('h',0,1) # [start,end)


# %%

a = [23, 45, 1, -3434, 234]

'''remove'''
a.remove(45)
print(a)
# 从[0]开始移除

'del'
del(a[0])
print(a)

'''reverse'''
a.reverse()
print(a)
print(a[::-1])


'sort'
# a.sort()
# print(a)

sorted(a)
l1 = [36 ,5,-12, 9, -21]
sorted(l1,key=lambda x:x**2)
sorted(l1,key=abs)

L = [['Bob',75],['Adam',92],['Bart',66],['Lisa',88]]
def by_name(t):
    return t[0]

list(map(by_name,L))
sorted(L,key=by_name)




# %%
# 栈：last in first out

'pop'
c = list(range(6))
c.pop()
print(c)
c.pop(2)

# 队列：first in first out
c.pop(0)


# %%
# 列表推导式

squares = [x ** 2 for x in range(10)]
squares

[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]

# 列表的嵌套
l3 = range(1,4)
[x  +1 for x in [x **2 for x in l3]]


# %%
# 高阶函数
'map'
# 双参数，f&iterator,返回iterator
def f(x):
    return x * x
list(map(f,range(10)))

print(list(map(lambda x:x**2,range(10))))

'filter'
# 双参数，f&iteratro,f返回True/False
list(filter(lambda x: x % 2 ==0, range(10)))

def noempty(s):
    return s and s.strip()
l2 = ['a',' b',None,'c ','',' ']
list(filter(noempty,l2))

#回文数字
def is_p(n):
    return int(str(n)[::-1]) == n 
list(filter(is_p,range(1,200)))

'返回函数'
def sum1():
    return lambda x,y: x+y
print(sum1()(2,3))

def sum2(x,y):
    return lambda: x+y
print(sum2(2,3)())

'reduce'
# 双参数，f&interator,累积运算
from functools import reduce

reduce(sum1(),d)

def prod(L):
    def pp(x,y):
        return x * y
    return reduce(pp,L) # 可用lambda函数

d = list(range(1,6))
prod(d)








# %%
'''Tuple'''
a = 'Adam', 'Brant', 'Chris'
a
x, y = divmod(15, 2)
y

a1 = (123)
type(a1) # int
a2 = (123, )
type(a2) # tuple


'''SET'''
basket = {'apple','orange', 'apple', 'pear'}
basket # 去除重复元素
'orange' in basket

s1 = set('abracadabr')
s2 = set('alacazam')
s1 - s2
s1 | s2
s1 & s2

basket.pop() # 随机删除
basket.add('banana')

'''dictionary'''
# 键值对{key:value}集合
data = {'a1':9, 'a2':8, 'a3':[7]}
data['a1']


data['a4'] = 6
del(data['a2'])
data

'a3' in data

data2 = dict(b1 = 6, b2= 7, b3= 8 )
for k,v in data.items():
    print('{} uses {}'.format(k,v))

# value添加数据 .setdefault(key,default)
data.setdefault('a3',[]).append(9)
data.setdefault('a3',[]).append('python')
data

'''获取索引'''
for i,j in enumerate(list(range(10,13))):
    print(i)

'''同时遍历2个序列'''
[i * j for i,j in zip([1,2,3], [10,11,12])]


# %%
'''数据结构'''
n = int(input('Enter the nubmer of students'))
data = {}
subjects = ('Physics', 'Math', 'History')

for i in range(n):
    name = input('Enter the name of student{}'.format(i + 1))
    marks = []
    for k in subjects:
        marks.append(int(input('Enter the mark of {}'.format(k))))
    data[name] = marks

for x, y in data.items():
    total = sum(y) 
    print('{}\'s total marks {}'.format(x, y))
    if total < 120:
        print(x, 'Falied:(')
    else:
        print(x, 'Passed:)')


# %%
'''porduction of matrix'''
# n = int(input('Enter the rank of matrix'))
# print('Enter the values of matrix A')
# A = []
# for i in range(n):
#     A.append([int(x) for x in input().split()]) # str.split(str="",number=-1)

# print('Enter the values of matrix B')
# B = []
# for i in range(n):
#     B.append([int(x) for x in input().split()])

C = []
for i in range(n):
    C.append([A[i][j] * B[i][j] for j in range(n)]) # 列表嵌套，添加

print('After matrix multiplication')
print('-' * 7 *n)
for x in C: 
    for y in x:  # 嵌套列表
        print(str(y).rjust(5), end=' ') # str.rjust(width)
    print()  # 换行
print('-' * 7 *n)


# %%
d = []
d1 = []
for i in range(3):
    for j in range(3):
        d1.append(A[i][j] * B[i][j])
    d.append(d1)
d


