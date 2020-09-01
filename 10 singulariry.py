# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
'''
SyntaxError # 語法錯誤
IndentationError # 縮進
NameError # 未定義變量
TypeError # 操作應用于不適當類型的對象 int + str
'''


# %%
'''執行try語句，若有異常，後續try子句停止執行
A 匹配except,執行except語句
B 沒有except匹配，則返回上一級的try語句中。直到程序終止，顯示信息（未處理異常）
'''

def func():
    x = 10 / float(input('Enter a number: '))
    return x

for i in range(4):
    try:
        print(func())
    except ValueError: # 空的except 捕獲任何error
        print('you entered a wrong number')


        


# %%
'''raise, finally, with'''
try:
    raise ValueError('a value error')
except ValueError:
    print('ValueError in code.')
finally:
    print('byebye')


#  with open(path) as nb:
#      pass

# try :
#     nb = open(path)
#     pass
# finally:
#     nb.close()


# %%
import sys

def Hours(u):
    
    if u < 0 :
        raise ValueError
    h, m = divmod(u, 60)
    # print('{}H, {}M'.format(h, m))
    return h, m

try:
    Hours(int(sys.argv[1]))
    print('{}H, {}M'.format(*Hours(int(sys.argv[1]))))
except ValueError:
    print('Parameter Error')


