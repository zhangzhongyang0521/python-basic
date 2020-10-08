# int(x) 将x转为整数类型
print(int(18.963))
# float(x) 将x转为浮点数类型
print(float(18))
# complex(real[,imag]) 创建复数
print(complex(13, 25))
# str(x) 将x转为字符串
print("age:" + str(25))
# repr(x) 将x转为表达式字符串
print(repr(1856392))
# eval(str) 计算字符串中的有效python表达式,并返回一个对象
print(eval('10+20'))
# chr(x) 将整数x转为字符
print(chr(97))
# ord(x) 将字符x转为对应的数值
print(ord('a'))
# hex(x) 将整数转为十六进制字符串
print(hex(965))
# oct(x) 将整数转为八进制字符串
print(oct(965))

# 模拟超市抹零操作
total_money = 56.75 + 72.91 + 88.50 + 26.37 + 68.51
print("total money:" + str(total_money))
real_money = int(total_money)
print("real money:" + str(real_money))
