# 整数数据类型
# 十进制整数
print(31415926535897932384626)
print(66666666666666666666666666666666666666666666666666666666666666666)
print(-2018)
print(0)
# 八进制整数,以0o/0O开头
print(0o123)
print(-0O124)
# 十六进制整数,以0x/0X开头
print(0x25)
print(0Xb01e)
# 二进制整数,以0b/0B开头
print(0b101)
print(0B1010)

# 浮点数据类型
print(0.1 + 0.1)
print(0.1 + 0.2)  # 因为浮点数计算的不准确性，结果为：0.30000000000000004，并非0.3

# str()函数将数值转为字符串表现形式
value = 18
# print("age:" + value) # python中不能直接简单的相加，会导致TypeError: can only concatenate str (not "int") to str
print("age:" + str(value))
if value>=18:
    print("你成年啦！")

# 复数，由实部+虚部组成，使用j或J表示虚部
print(3.14+12.5j)

# 字符串的三种定义形式，'aa'或"aa"或'''aa''',其中'''aa'''字符串可分开为多行
print('aa')
print("aa")
print('''aa''')
print('''萱萱宝宝，你要健健康康地
茁壮成长！''')
# 字符串中也可以嵌套使用引号
print('在python中可是使用"value"的形式定义字符串')

# 转义字符
# \ 续行符
result = "接口请求的结果是\
{status:200,result:true}"
print(result)
# \n 换行符
print("great\npython")
# \0 空
print("great\0python")
# \t 水平制表符
print("great\tpython")
# \" 双引号
print("\"python\"")
# \' 单引号
print('\'python\'')
# \\ 反斜杠
print("\\python\\")
# \f 换页
print("great\fpython")
# \0dd 八进制数
print("great\012python")
# \xhh 十六进制
print("great\x0apython")
# 使用r或R，那么字符串会将原样输出，其中的转义字符不进行转义
print(r"great\x0apython")

# 布尔类型，python中True和False被解释为布尔值，布尔值也可转为数值，True表示为1，False表示0
# python中数值0可表示为false
flag = 0
if flag:
    print("true")
else:
    print("false")