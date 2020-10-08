# 运算符
# 算数运算符
# + 加法
print(10 + 21)
# - 减法
print(60 - 59)
# * 乘法
print(5 * 6)
# ** 幂运算
print(2 ** 4)
# / 除法，除数不能为0
print(7 / 2)
# % 求余，即返回余数
print(10 % 3)
# // 取整数，即返回商的整数部分，除数不能为0
print(7 // 2)

# 赋值运算符
# = 简单的赋值运算符
value = 20
print(value)
# += 加赋值
value += 2
print(value)
# -= 减赋值
value -= 10
print(value)
# *= 乘赋值
value *= 2
print(value)
# **= 幂赋值
value **= 2
print(value)
# /= 除赋值
value /= 9
print(value)
# //= 取整赋值
value //= 5
print(value)
# %= 取余赋值
value %= 2
print(value)

# 比较运算符
# > 大于
print(10 > 2)
# >= 大于等于
print(5 >= 6)
# < 小于
print(8 < 18)
# <= 小于等于
print(190 <= 168)
# == 等于
print('a' == 'b')
# != 不等于
print('y' != 't')
# 区间范围
print(-1 <= value <= 10)

# 逻辑运算符
print("logic operation")
# and 逻辑与
value = (1 >= 2) and (9 <= 20)
print(value)
# or 逻辑或
value = (1 >= 2) or (9 <= 20)
print(value)
# not 逻辑非
value = not (9 <= 20)
print(value)

# 位运算
# & 位与运算
print(12 & 8)
# | 位或运算
print(4 | 8)
# ^ 位异或运算
print(31 ^ 22)
# ~ 位取反运算
print(~123)
# << 位左移运算，即乘以2的n次方
print(48 << 2)
# >> 位右移运算，即除以2的n次方
print(-80 >> 2)

# 模拟手机店打折活动
print("大成新开手机店促销活动")
week = input("星期几过来？")
time = int(input("几点过来？"))
condition1 = week == "星期二" and (10 <= time <= 11)
condition2 = week == "星期五" and (14 <= time <= 15)
if condition1 or condition2:
    print("来对咯，您嘞")
else:
    print("来的太迟的，没有了")
