'''单行多个赋值'''
data = ('shiyanlou', 'China', 'Python')
name, country, language = data
print(name)
# R侧元组封装， L侧tuple unpacking

a, b = 0, 23
a, b = b, a
print(a, b)


