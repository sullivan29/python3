# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
'''
所有數據類型均可視爲對象object；自定義對象數據類型class
'''

class myclass(object):
    '''a simple example class'''
    u = 123 # 類屬性 attribute
    def f(self): # 方法 method
        return 'hello world'

mc = myclass()
mc.f()


# %%
'''__init__ 將類實例化的函數符號，無參數函數'''
# 創建對象有初始屬性，參數

class complex:
    def __init__(self,realpart,imagepart):
        self._u = 'inital'
        self.r = realpart
        self.i = imagepart
c = complex(4,-5)
c._u # 私有變量
# c.i


# %%
'''繼承父類的所有功能（變量和方法）'''


class Person():
    '''
    返回具有給定名稱的Persion對象
    '''

    def __init__(self, name, age=16): # 默認參數age 在位置參數之後
        self.name = name
        self.age = age
        self.year = 2020-self.age
        
    def get_details(self):
        return self.name, self.age


class Student(Person):
    '''
    返回Student對象，name, branch, age 3個參數
    '''

    def __init__(self, name, branch, age=19):
        super().__init__(name, age) # 父類屬性 name age 
        self.name = name
        self.age = age
        self.branch = branch

        
    def get_details(self):
        return '{} student majors in {} and age {} is born in {} year, '.format(self.name, self.branch, self.age, self.year) 
        # 非參數 self.year 繼承父類
        # 參數 name age 顯性 __init__()



person1 = Person('Ailsa') # 默認參數 age
person1.get_details()

student1 = Student('Angela', 'CSE', 17)
student1.get_details()

class Teacher(Person):

    def __init__(self, name, age):
        self.name = name
        self.age = age
    # get_details 繼承父類

teacher1 = Teacher('Caroline', 18)
teacher1.get_details()


# %%
'''test super().__init__()'''


class Root(object):
    def __init__(self):
        self.x = '屬性'
        self.y = 3

    def fun(self):
        print(self.x)
        print('方法')


class A(Root):
    def __init__(self):
        print('實例化')

r = Root()
r.fun()

atest = A()
# atest.fun() 實例無屬性 x


class B(Root):
    def __init(self):
        super().__init__()
        print('實例化')

btest = B()
btest.fun()
btest.y


# %%
class Dog(object):
    def run(self):
        print('dog runs fast')


def run3(TT):
    TT.run()
    TT.run()
    TT.run()

run3(Dog())


# %%
'''多態'''

class Animal():
    pass

class Mammal(Animal):
    def run(self):
        print('Mammal is running')

class Bird(Animal):
    def fly(self):
        print('Bird is flying')

class RunnableMixin(Animal):
    def run(self):
        print('Running')

class Cat(RunnableMixin, Mammal):
    pass

Cat().run() # 相同屬性/方法，1st父類優先
run3(Cat())


# %%
'''刪除對象'''
# del 對象引用計數-1

s = 'test note'
del s
s


# %%
'''屬性獲取和刪除'''

class Ss(object):
    def __init__(self):
        self.x=8
    def power2(self):
        return self.x*self.x
    def add2(self,tt):
        return tt+tt
    name = 'test'

b = Ss()
c = Ss()

hasattr(b, 'x')
setattr(b, 'y', 5) # b.y = 5
b.add2(b.y)

ff = getattr(b, 'add2') # ff = b.add2
ff(7)

hasattr(Ss,'add2')
hasattr(Ss, 'name')
b.name


# %%
'''增刪 實例屬性和類屬性'''
class Student(object):
    def __init__(self):
        self.name = 'instance attr'
    name = 'class attr'

s = Student()
print(s.name) #实例name
print(Student.name)#class name

# s.name = 'Michael'# 实例绑定name属性
# print(s.name)
# print(Student.name)

del s.name
print(s.name)
hasattr(Student, 'name')

# del Student.name

'''添加 實例和類的方法'''
# 無法刪除？

class Rr():
    def __init__(self, x):
        self.x = x
    pass


def plus1(self, t):
    return t+1
Rr.u = plus1
d1 = Rr(9)
d1.u(7)

hasattr(d1, 'u')
hasattr(Rr, 'u')

# def minus1(self):
#     return self.x-1
# Rr.z = minus1
# d2 = Rr(9)
# d2.z()




# %%
'''property定義函數，setter獲得屬性參數'''
# 無法del
class Screen(object):

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def resolution(self):
        return self._width * self._height

    @width.setter
    def width(self, value):
        self._width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise ValueError('Must be integer')
        self._height = value


s = Screen()

s.width = 20

s.width
s.height = 3

s.height
s.resolution



# %%
'''return '''

class Account(object):
    '''賬號，美元金額'''

    def __init__(self, rate):
        self.__amt = 0
        self.rate = rate

    @property
    def amount(self):
        return self.__amt

    @property
    def cny(self):
        return self.__amt * self.rate

    @amount.setter
    def amount(self, value):
        if value < 0:
            print('no negative amount')
            # raise ValueError
            return 
        self.__amt = value

acc = Account(rate=6.6)
# acc.amount = 100
# print('Dollar amount', acc.amount)
# print('In Cny',acc.cny)
acc.amount = -10
print('Dollar amount', acc.amount)


