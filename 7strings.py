# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
'''分行输入，拼接'''
s = 'Here is line split in two lines.'
s
'''换行'''
s2 = 'Here is line \n split in two lines.'
s2
print(s2)


# %%
'''分行输入，分行output'''
s3 = '''        Usage: thingy [options]
        -h                        Display the message
        -H hostname               Hostname to connect to'''
print(s3)
s3


# %%
'''标题'''
s4 = 'shi yan lou'
s4.title()
s4.upper()
s4.lower()

s5 = 'I am A pRoGramMer'
s5.swapcase()

'''is alpha, digit, lower, title'''
# alnum, alpha, digit 不含space
s6 = 'timeisnow'
s7 = str(1234)
s6.isalnum()
isinstance(s6,(str,list))
s5.isalnum()

s6.isalpha()
s7.isdigit()

s4.lower().islower()
s4.upper().isupper()
s4.upper().istitle()


# %%
'''split& join'''
ss1 = 'we are waiting'
ss1.split() # 返回 list
ss1.split('a')

'-'.join('python is great'.split())

'''strip'''
# strip 空格和换行
ss2 = ' awww.foss. cn\n'
ss2.strip()

ss2.lstrip(' wnas.')
# stirp chars中包含的任意characters


# %%
'''搜索'''
ss3 = 'faulty for reason'
ss3.find('lty') # 返回索引
ss3.find(' for')
ss3.find('fra')

ss3.startswith('fau')
ss3.endswith('son')

ss4 = input('Enter a string: ')
if ss4[::-1] == ss4:
    print('this is a palindrome')
else:
    print('this string isn\'t a palindrome')

'''len'''
ss1 = 'we are waiting'
print(' the number of words in this line is %d'%(len(ss1.split())))
print(' the number of words in this line is {}'.format(len(ss1.split())))


# %%



