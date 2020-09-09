#!/usr/bin/env python3

import sys
from collections import Counter

class Person(object):
    """
    返回具有给定名称的 Person 对象
    """

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def get_details(self):
        """
        返回包含人名的字符串
        """
        return self.name
    
    def get_grade(self):
        '''
        返回成绩
        '''
        return self.grade


class Student(Person):
    """
    返回 Student 对象，采用 name, branch, year 3 个参数
    """

    def __init__(self, name, branch, year, grade):
        Person.__init__(self, name, grade)
        self.branch = branch
        self.year = year

    def get_details(self):
        """
        返回包含学生具体信息的字符串
        """
        return "{} studies {} and is in {} year.".format(self.name, self.branch, self.year)
    
    def get_grade(self):
        lis1 = []
        for k in self.grade:
            assert k in 'ABCD'
            if k == 'D':
                lis1.append('Fail')
            else:
                lis1.append('Pass')
        
        c2 = Counter(lis1).most_common() # Counter:字典类  most_common:列表
        for k in c2:
            print('{}: {}'.format(k[0],k[1]), end= ' , ')
        return 


class Teacher(Person):
    """
    返回 Teacher 对象，采用字符串列表作为参数
    """
    def __init__(self, name, papers, grade):
        Person.__init__(self, name, grade)
        self.papers = papers

    def get_details(self):
        return "{} teaches {}".format(self.name, ','.join(self.papers))

    def get_grade(self):
        c = Counter(self.grade).most_common()
        for k in c:
            assert k[0] in 'ABCD'
            print('{}: {}'.format(k[0],k[1]), end= ' , ')
        return 


person1 = Person('Sachin', 'ABD')

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Wrong Arguments')
        sys.exit(1)
    else:
        if sys.argv[1] == 'student':
            student1 = Student('Kushal', 'CSE', 2005, sys.argv[2])
            student1.get_grade()
        elif sys.argv[1] == 'teacher':
            teacher1 = Teacher('Prashad', ['C', 'C++'], sys.argv[2])
            teacher1.get_grade()
        else:
            print('Wrong sys parameters')
