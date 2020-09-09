"""
缩进(indentation) 续行时，与分隔符(delimiter)-括号对齐；or至于code块内部。
if 条件语句续行时，添加L括号，并在2nd行缩进。
recommend使用括号内隐式换行，instead of \。

多行结构中，\"""&R括号至于最后一行1st字符下方。
断行在二元操作符后面。
每行79/72字符。
3引号使用"。

import 在文件顶部，__doc__之后。不同模块独立成行。
避免导入通配符*。
"""

"""
空行：函数和类 2空行，类内方法1空行。
空格：与括号、后面的逗号、冒号等保持紧凑；冒号两侧空格相当: def fun(x):, lis1[1::3].
二元操作符两侧+空格：= += == > in is and or not
低优先级的操作符两侧+空格：f = x*2 - 1, c == (a+b) * (a+b)
关键值/默认值数两侧无空格：def complex(real, imag=0): return magic(r=real, i=imag)
冒号单独空格，带注释的函数定义=两侧+空格：def munge(sep: Anystr = None)
"""

"""
注释  # 空格
短语时，首字母大写，可省略句点；句点后2空格。
行内注释  空2格#
"""
"""
版本注记 在文档字符串后
__version__ = '$Revision$'
"""


"""
命名约定
避免lOI等易于10混肴的变量名。
Module命名短、lower，package命名不用下划线。
异常是 class，用error作为异常名的后缀。
全局变量 用__all__标明可导出的全局变量。
函数名 lower+underscore。
Method 第一个参数：self
常量 UPPER
继承 double前导uderscore，属性不会被子类继承。公有属性，不应有前导underscore。Easier变公有属性
"""

"""
公共和内部接口
__all__明确规定公有API的名字。
内部接口(包、module、类、函数、属性)应有前导underscore，内部接口的空间是内部的。
"""
