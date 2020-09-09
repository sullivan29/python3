# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
'''collections模块
Counter类 散列计数的dict key:元素，value:计数'''

from collections import Counter
# help(collections.Counter)
# print(collections.Counter.__doc__)

c = Counter('abcdeabcdabcaba') # instance c
c.most_common(3)

sorted(c) # 返回list
''.join(sorted(c.elements())) # str list elements with repetitions
sum(c.values())

c['a']


d = Counter('tab lab')
d['b'] -= -1

c.update(d)
c


# %%
'''正则re'''
import re
s2 = 'abe 29facad0a'

'''^$start,end'''
re.findall('a.', s2) # a后1字符(except换行)
re.findall('^a.', s2)
re.findall('a.$', s2)

'''贪婪匹配'''
re.findall('a.?', s2) # a后任意0/1次
re.findall('a.*', s2) # a后任意0/infinite次
re.findall('.*a$', s2)

re.findall('a.+', s2) # a后1/infinite次
re.findall('a.{1,2}', s2) # a后2次(priority) 


'''惰性匹配'''
re.findall('a.{1,2}?', s2)
re.findall('a.??', s2)
re.findall('a.*?d', s2)  # 任意次，尽可能少，至d

'''字符集'''
re.findall('a[be f0c]*', s2) # a后0/infinite次
re.findall('a[^f]*', s2) # 不是f0/infinite次
re.findall('[\d]+', s2)


s3 = '112345x'
s4 = '1123456' 
s5 = '1123'
'''分组() 或|'''

re.fullmatch('^[1-9]\d{3,5}[0-9x]$', s3).group() # start1-9,总位数7(x) or 4
re.fullmatch('^[1-9]\d{3}(\d{2}[0-9x])?$', s5).group() # ()分组

re.fullmatch('^[1-9](\d{5}[0-9x]|\d{3})$', s5).group() # |或


# %%

import re

st1 = "匹配s规则这s个_79字 /S符 串规则-/455则"
# re.findall('[^a-z]', st1) # 返回list
# re.findall('.则$', st1)
# re.findall('规则.*', st1) # *元字符
# re.findall('规则.{2,}?', st1)
# # re.findall('匹配[s,f]规则', st1) # []字符集内任意匹配

# # re.findall('\D+', st1) # [^0-9]

# st3 = "匹配s规则这s个_字 /S符 \n \t \f \v串规则nnm-/455则" 
# # re.findall('\s', st3) # 空白字符 
# re.findall('\S', st3) # [^\t\n\f\v]


# re.findall('\w', st1) # 字母数字汉字下划线
# re.findall('\W', st1)

# st4 = 'aaa123cde\t'
# re.search('([a-z]+)(\d+)([a-z]+)(\s)', st4).group() #获得相应分段字符


''' r 去除特殊意义如\n 转成原生(raw string)字符\和n
用于正则和系统路径'''

st5 = 'F:\English\math\nMoney'
# re.findall(r'\n.+', st5)
st5  #'F:\\English\\math\nMoney' 注意double \\ 转义\

'''compile将规则编译为对象'''
'''search,match 返回第一个match对象 str'''

st1 = "匹配s规则这s个_79字 /S符 串规则-/455则"
# re.search('规则.*?/', st1).group() # 返回第一个match对象 str
# re.match('匹.*?规则.*?/', st1).group() # 从索引0开始


'''findall
无分组：所有合规字符
有分组: 匹配组内字符'''

'''
group() 返回re.search/match对应字符(无论是否分组)；groups()返回组内字符tuple
'''
com2 = re.compile(r'规.{3,}?')
com2.findall(st1) # 返回str列表

com3 = re.compile(r'规则(.*?)规则(.*)')
com3.findall(st1) #[('这s个_79字 /S符 串', '-/455则')] 
com3.search(st1).groups()

# com = re.compile(r'(规则.*?\d)(\d*)')
# com.findall(st1) #[('规则这s个_7', '9'), ('规则-/4', '55')]

'''split, sub'''
re.split('规则', st1)
re.split('则\w', st1)

re.sub('s', 't', st1) # str.replace


# %%
'''
read  findall('\w')  Counter
'''

from collections import Counter
import re

path = r'e:\coding\test.txt'
with open(path, 'r') as nb:
    words = nb.read().upper()
    words = re.findall('\w+', words)
    
    print(Counter(words).most_common(4))
   


# %%
'''命名元组'''

from collections import namedtuple

Point = namedtuple('Point', ['s', 't']) 
''' return a subclass of tuple ,parameters: typename, field_names'''
u = Point(12, t=40)
u.t % u.s

divmod(u[1],u[0])



