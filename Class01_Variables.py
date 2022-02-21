# edit with IDLE python 如何使用python官方编辑器
# Python systax 基础语法
# print "Hello World!" 2.7
# print("Hello World!") 3.9
# Variables 变量的命名 字母数字下划线
n = 'This is a text'
m = 'This is another text'
a = 10
b = 20.1
print a, b, a+b
type(a)
year = 2021  # right
Year = 2021  # right
# 2021_year = 2021  # wrong
vars()  # 查看内存已有的变量
del a  # 删除指定的变量

c = 15.1
d = int(c)

e = 15
d = float(e)

# 简单的math
e+d
e-d
e*d
e/d
e**2
help(type)

# 简单控制语句
for i in range(2000, 2021, 1):
    print i 

for i in range(2021, 2000, -2):
    print i 
