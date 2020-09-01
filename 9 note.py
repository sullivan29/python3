# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# 文本文件 & 二进制文件
import os
os.getcwd()

# nt1 = open('test.txt') # file 对象
# nt1.read() # 一次性读取，size return 字符串

# nt1.close()

nt2 = open('test.txt')
nt2.readlines() # return 列表
# readline只能读1行 return 字符串，保持当前内存
nt2.close()

# nt = open('test.txt')
# for k in nt:
#     print(k)
# nt.close()


# %%

with open('test.txt','w') as nt3:
    nt3.write('time to get new things.\nmiss the point\nIt\'s saft to assume\nI\'m at risk')

with open('test.txt','r') as nt3:  
    print(nt3.read())

# with open('test.txt') as nt4:
#     for k in nt4.readlines():
#         print(k, end='')


# %%
#!/usr/bin/env python3
import sys
if len(sys.argv) < 3:
    print('Wrong parameter')
    print('./copyfile.py file1 file2')
    sys.exit(1)
f1 = open(sys.argv[1])
s = f1.read()
f1.close()

f2 = open(sys.argv[2],'w')
f2.write(s)
f2.close()


tt = sys.argv[0]
print(tt)
# argv 程序从外部获取参数额桥梁，return列表。将程序保存，从（命令行）外部给出参数

print('first value',sys.argv[0])
print('all values')
for i, x in enumerate(sys.argv):
    print(i, x)


# %%
'''try except finally'''
#  执行except分支
try:
    print('try...')
    r = 10/int(input('Enter a number: '))
    print('result', r)
# except ValueError as e:
#     print('ValueError', e)
except ZeroDivisionError as e:
    print('Zero', e)
finally:
    print('fianlly')
print('End')


# %%
'''sys.exit exit os.exit'''
import sys, os

#线程中退出，终止python程序
try:
    os.exit() # defaults: 0
except:
    print('die.')
finally:
    print('cleanup')

# raise SystemExit,若异常未被捕获，则退出python。

# try:
#     sys.exit(101)
# except SystemError as e:
#     print(repr(e))
# finally:
#     print('cleanup')


# %%
import os, sys

def parse_file(path):
    '''
    分析文本，返回单词数、空格、制表符、行数
    '''
    tb = open(path)
    # print(tb.readlines()) # 不可与enumerate混用，猜测read, write等改变状态

    i = 0
    letters = 0
    spaces = 0
    tabs = 0
    
    for i, line in enumerate(tb): # enumerate(iterable)
        spaces += line.count(' ')
        tabs += line.count('\t')
        letters += len(line.split()) # split 分离 space,\n,\t 返回列表
    
    tb.close()
    return letters,spaces, tabs, i+1


with open('./test.txt') as ttb:
    print(ttb.read())

print(parse_file('./test.txt'))


# %%

def main(path):
    '''
    打印分析结果
    :arg path: 文本路径
    :return:文本存在为True
    '''
    if os.path.exists(path):
        letters, spaces, tabs, lines = parse_file(path)
        print('Letters {}. Spaces {}. tabs {}. lines {}'.format(letters, spaces, tabs, lines))
        return True
    else:
        return False

main('./test.txt')

if __name__ == '__main__':
    if len(sys.argv) > 1:
        mainf(sys.argv[1])
    else:
        sys.exit(-1)
    sys.exit(0)


# %%
'''dict计数字符'''

s1 = ' abtenm t'
d = dict()
for i in s1:
    d[i] = s1.count(i)
d



# %%
with open('./test.txt') as tbb:
    # for line in tbb: # in tbb.readlines()
    #     print(line)
    print(tbb.readline(2)) # size
    # print(tbb.readline())
    


# %%
with open('./test.txt') as tbb:
    
    while True:
        tr = tbb.readline()
        if tr:
            print(type(tr), tr)
        else:
            break
        


# %%
s = str('ab10c 8\nm9 ')
# s.index('1')

# b = 'time'
# s.join(b) # s插入到b ,b 可迭代

# ''.join([s,b])

''.join([s[i] for i, t in enumerate(s) if t.isdigit()])




