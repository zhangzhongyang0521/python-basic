# break语句，终止当前循环
# break在while循环中的语法
# while 条件表达式1:
#     执行代码
#     if 条件表达2:
#         break
# break在for循环中的语法
# for 迭代变量 in 对象:
#     if 条件表达式:
#         break
# 改良版for求数
print("求数，三三数之剩二，五五数之剩三，七七数之剩二")
for number in range(100):
    if number % 3 == 2 and number % 5 == 3 and number % 7 == 2:
        print("found:" + str(number))
        break

# continue语句，只能终止本次循环而提前进入下次循环
# continue在while循环中的语法
# while 条件表达式1:
#     执行代码
#     if 条件表达2:
#         continue
# continue在for循环中的语法
# for 迭代变量 in 对象:
#     if 条件表达式:
#         continue
# 计算逢7拍腿游戏，共拍了几次腿
total = 99
for number in range(1, 100):
    if number % 7 == 0:
        continue
    else:
        string = str(number)
        if string.endswith('7'):
            continue;
    total -= 1
print("共拍了", total, "次")

# pass空语句，一般起到占位作用，不做任何事情
for number in range(1, 10):
    if number % 2 == 0:
        print(number, end=' ')
    else:
        pass
