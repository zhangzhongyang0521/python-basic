# 简单if语句：
# if 表达式:
#   语句块
print("求数，三三数之剩二，五五数之剩三，七七数之剩二")
number = int(input("哪个数？"))
# python中if语句块后必须加:,否则会出现SyntaxError: invalid syntax错误
if number % 3 == 2 and number % 5 == 3 and number % 7 == 2:
    print(number, "符合条件！")
# python中if可带多个语句但必须要有正确缩进
value = 98
if value > 100:
    print("大于100")
    print("数据异常")
print("没有正确缩进，所有不在上面的if语句块中")

# if···else语句:
# if 表达式:
#   语句块1
# else:
#   语句块2
result = -9
if result > 0:
    absResult = result
else:
    absResult = -result
print(absResult)
# 上述语句的简洁写法(专业说法:条件表达式)
absResult = result if result > 0 else -result
print(absResult)
# else语句不能单独存在，根据其缩进可以判断其属于哪个if语句
if result >= 0:
    if result > 0:
        print("大于0")
    else:
        print("等于0")

# if···elif···else语句
# if 表达式1:
#     语句块1
# elif 表达式2:
#     语句块2
# elif 表达式3:
#     语句块3
# ···
# else:
#     语句块n
print("玫瑰集爱情与美丽于一身，不同朵数的玫瑰花代表不同的含义")
count = int(input("送几朵?"))
if count == 1:
    print("你是我的唯一")
elif count == 3:
    print("I LOVE YOU")
elif count == 10:
    print("十全十美")
else:
    print("不晓得了")

# if语句的嵌套
print("开酒不喝车，喝车不开酒")
proof = int(input("100ml血液里多少马尿?"))
if proof < 20:
    print("没卵事，注意行车安全")
else:
    if 20 <= proof < 80:
        print("你完了，酒后驾驶")
    else:
        print("醉驾了，小单间伺候")