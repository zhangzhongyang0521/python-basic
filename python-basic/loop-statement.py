# while循环，语法如下
# while 条件表达式:
#     循环体
print("求数，三三数之剩二，五五数之剩三，七七数之剩二")
found = False
number = 0
while not found:
    number += 1
    if number % 3 == 2 and number % 5 == 3 and number % 7 == 2:
        print("数字为", str(number))
        found = True

# for循环，语法如下
# for 迭代变量 in 对象:
#     循环体
print("计算1+2+3+···+100=?")
result = 0
# range内置函数，用于生成一系列连续的整数，语法:range(start,end,step)
# range函数中start可省略(默认为0)，step可省略(默认为1)，end不可省略(生成的数据不包括end)
for i in range(101):
    result += i
print("结果为", result)
# 使用range函数输出10以内的奇数，print时使用end=' '将内容打印在一行，不换行
for i in range(1, 10, 2):
    print(i, end=' ')
print("\n再求数，三三数之剩二，五五数之剩三，七七数之剩二")
for value in range(100):
    if value % 3 == 2 and value % 5 == 3 and value % 7 == 2:
        print("数字为", value)
# 变量字符串
content = "LOVE"
print(content)
for char in content:
    print(char)

# 嵌套循环，for循环和while循环可以互相嵌套
# 打印九九乘法表
for row in range(10):
    for col in range(1, row + 1):
        print(str(row) + "*" + str(col) + "=" + str(row * col) + "\t", end='')
    print("")
