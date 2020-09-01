# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
'''
Bars Module
==================
'''
def starbar(num):
    '''
    打印*分隔线
    :arg:num 线长
    '''
    print('*'*num)

def hashbar(num):
    '''
    打印#分割线
    :arg:num线长
    '''
    print('#'*num)


# %%
'''模块：python定义和声明的文件'''

import Bars
Bars.hashbar(5)

from Bars import starbar
starbar(4)


# %%
'''包：含__init__.py的目录，所有.py文件均为子模块'''

from mymodule.Bars import starbar

starbar(6)


# %%
'''
help()
获得modules, keywords, symbols, topics
'''


# %%
'''os'''

import os

os.name
os.getcwd()
os.listdir()
# os.mkdir('./new')
os.chdir('e:\\coding')
# os.remove('utils.py')

os.path.exists('e:\\coding\\test.txt')
os.path.isfile('e:\\coding\\test.txt')
os.path.basename('e:\\coding\\test.txt')
os.path.dirname('e:\\coding\\test.txt')

d, f = os.path.split('e:\\coding\\test.txt')
print(d, f)
os.path.join(d, f)

os.path.getsize('e:\\coding\\test.txt')
# os.path.normpath('e:\\coding\\test.txt')



# %%
'''sys'''

import sys

# sys.argv
sys.getdefaultencoding() # 系统当前编码

sys.path # 模块搜索路径集合

sys.platform # 系统平台

for i in range(10):
    print('第{}次：'.format(i), i)
    if i == 5:
        print('第{}次退出'.format(i))
        sys.exit(1)


# %%
'''time'''
import time

# 时间戳
ticks = time.time()

# struct_time 有命名元组接口的对象 st2.tm_mon
time.localtime(ticks)
st2 = time.localtime()
t2 = time.mktime(st2)

# 格式化时间
time.asctime(st2)
s2 = time.strftime('%Y %m %d %H %M', st2)
time.strptime(s2, '%Y %m %d %H %M')

time.ctime(st2)


# %%
import subprocess
# subprocess.call('conda list', shell=True)
# subprocess.check_output('conda list')

# subprocess.call('python test2.py') # 返回状态码 0/1
subprocess.check_output('python test2.py')# 返回执行结果 or 抛出异常


# %%
'''requests HTTP库'''

import requests

def download(url):
    '''
    指定url下载文件并存储至目录
    url：网址
    '''
    try:
        req = requests.get(url)
    except:
        print('Invalid URL"{}"'.format(url))
        return
    if req.status_code == 403:
        print('you do not have acces')
        return
    filename = url.split('/')[-1]
    with open(filename, 'w') as nt:
        nt.write(req.content.decode('utf-8'))
    print('Download over.')

# __name__ == __main__ 当模块执行(名为__main__)时，执行if块。
# 当作为模块import时，不执行if块。
if __name__ == '__main__':
    url = input('enter a url: ')
    download(url)


# %%
'''return 返回'''

def fun():
    print('test')
    return

r = fun() # 函数返回 None 给r；本语句无返回值，不输出。print test
print(r) # print None



# fun() #执行函数，print test, 但是 返回值None不显示
# print(fun()) # print  test None


# %%
import requests
r1 = requests.get('http://httpbin.org/get')
print(r1.text)

print(r1.json())
type(r1.json())


# %%
'''argparse模块 实现linux ls功能'''


