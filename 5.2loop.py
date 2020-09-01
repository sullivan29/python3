#!/usr/bin/env python3
# n = int(input('Enter the number of rows: '))
# while n > 0:
#     print('*' * n)
#     n -= 1

# n = int(input('Enter the number of rows: '))
# k = 1
# while k <= n:
#     print('*' * k)
#     k += 1

# n = int(input('Enter the number of rows: '))
# for k in range(n):
#     x = '*' * (n-k)
#     y = ' ' * k 
#     print(y + x)

'''list'''
# 列表中的元素，不必是同一类型
'''列表索引，切片'''
# a = [1, 342, 223, 'India', 'Fedora']
# print(a[-1])
# #切片不改变正在操作的列表
# print(a[:3]) # [)切片区间
# print(a[:])
# print(a[0::2]) # 步长

# '''列表元素相加'''
# b = [ 36, 89, 100, 45, -2]
# c = list(range(5))
# print(c+b) # 列表len增加
# new = []
# for k in range(len(c)):
#     new.append(c[k]+b[k])
# print(new)

'''列表索引/切片允许改变'''
# b[2:4] = [0, 1]
# print(b)

# '''value是否存在'''
# print(-2 in b)
# if b:
#     print('不是空列表')

'''列表嵌套'''
# a1 = list('abc')
# b1 = list('123')
# x = [a1,b1]
# print(x[0][1])

'''for loop'''
# c1 = list(range(0,15,3))
# for k in c1[::2]:
#     print(k)

'''continue'''
# while True: # 提供loop forever
#     n = int(input('Please enter an Integer: '))
#     if n < 0:
#         continue
#     elif n == 0:
#         break
#     else:
#         print('Square is ',n ** 2)
#     print('Goodbye')

'''for loop 中的else'''
# 检测循环是否执行完毕

# for k in range(5):
#     print(k)
# else:
#     print('gg')

'''sticks'''
sticks = 21
print('There are 21 sticks,you can take 1-4 number of sticks at a time.')
print('Whoever will take the last stick will loose.')
while True:
    print('Sticks left: ',sticks)
    if sticks == 1:
        print('You took the last sticks, you loose.')
        break # break 跳出循环
    sticks_taken = int(input('Take the sticks(1-4): '))
    if sticks_taken <= 0 or sticks_taken >=5:
        print('Wrong choice')
        continue # wrong choice & continue instead of assert 
    print('Computer took: ',(5 - sticks_taken), '\n')
    sticks -= 5