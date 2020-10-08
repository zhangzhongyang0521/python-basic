# 使用input()函数获取用户输入，默认接收的是字符串类型，需要显式的转为需要的类型
# name = input("你的名字:")
# print(name, type(name))
# age = input("你的年龄:")
# print(age, type(age))
# salary = int(input("你的工资:"))
# print(salary, type(salary))

# 使用print()函数输出内容
number1 = 20
number2 = 50
print(number1)
print("python input() & print()")
# 输出表达式的值
print(number2 if number2 > number1 else number1)
# 输出多个值,以空格隔开
print(number1, number2)
# 输出到文件
file = open(r"D:\\memo.txt", "a+")
print("print content to file", file=file)
file.close()