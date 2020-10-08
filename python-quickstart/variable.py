'''
python中变量的声明方式： 变量名 = value
python是动态语言，即无需事先定义变量的类型，直接赋值即可
'''
number = 24
nickname = "jack"

# 使用type()函数获取变量的类型
variable = "name"
print(type(variable))
variable = 1024
print(type(variable))

# 使用id()函数获取变量所指的内存地址
value = result = 1024
print(id(value))
print(id(result))