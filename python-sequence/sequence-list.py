# python中列表是由一系列按照特定顺序排列的元素组成，形式上所有元素放在[]内，列表中的元素类型可以互不相同
# 列表的创建
# 1、使用赋值运算符直接创建列表，语法：listname = [element1,element2,...elementn]
prices = [12.89, 8.86, 1.58]
words = [58, "Java8", "Python3"]
print(prices, words)
# 2、创建空列表
numbers = []
print(numbers, len(numbers))
# 3、创建数值列表，语法：list(data)
numbers = list(range(10, 15))
print(numbers)
# 列表删除，实际开发中并不常用，python自带的垃圾回收器会自动销毁不用的列表
del numbers
# print(numbers),列表删除之后就不能再引用，否则会出现NameError: name 'numbers' is not defined错误

# 访问列表元素
persons = ["关二哥", "李云龙", "小马哥", "光头强"]
# 输出整个列表
print(persons)
# 输出单个元素
print(persons[1])
# 输出当前星期名称
import datetime

week_days = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
current = datetime.datetime.now().weekday()
print("今天是", week_days[current])

# 遍历列表，语法： for item in listname:
for person in persons:
    print(person, end=" ")
print()
# 使用for循环和enumerate()函数可实现同时输出索引和元素内容
for index, person in enumerate(persons):
    print("第" + str(index + 1) + "位:", person)
# 每行显示两位人员
for index, person in enumerate(persons):
    if index % 2 == 0:
        print(person + "\t\t", end="")
    else:
        print(person + "\n")

# 向列表中添加元素，语法：listname.append(element)
machines = ["电视", "冰箱"]
machines.append("洗衣机")
print(machines)
# append()只能在列表后面添加元素，insert()可以在任意位置添加元素，但执行效率不高故不推荐使用
machines.insert(0, "太空舱")
print(machines)
# 使用extend()方法可以将一个列表中元素全部加到另个列表中
machines.extend(persons)
print(machines)

# 修改列表中的元素
machines[0] = "按摩椅"
print(machines)
# 删除元素
# 1、根据索引删除元素，语法:del listname[index]
del machines[1]
print(machines)
# 2、根据元素删除，语法:listname.remove(element) 当要删除的元素不存在时，会抛出异常
machines.remove("光头强")
# machines.remove("aaa") 因aaa元素不存在于列表中，抛出异常ValueError: list.remove(x): x not in list
print(machines)
# 最好的做法：删除前先判断元素是否存在于列表中
if machines.count("aaa") > 0:
    machines.remove("aaa")

# 对列表进行统计和计算
# 1、获取指定元素出现的次数，语法：listname.count(element)，只能精确匹配
print(persons.count("关二哥"))
# 2、获取指定元素在列表中首次出现的索引,语法：listname.index(element)
print(persons.index("李云龙"))
# 3、对列表中的元素进行求和，语法：sum(listname[,start]),start表示指定相加的参数默认为0（即列表中元素相加之后再加start）
grades = [98, 92, 100, 96, 94]
print(sum(grades))
print(sum(grades, 5))

# 对列表进行排序，使用sort()方法实现，语法:listname.sort(key=None,reverse=False)
# 其中key为比较的键，例如设置 key=str.lower 表示排序时不区分大小写
# 其中reverse表示是否降序排序，默认为False(升序排列)
print(grades)
grades.sort()
print("升序:", grades)
grades.sort(reverse=True)
print("降序:", grades)
# 排序字母时不区分大小写,区分大小写时，先对大写字母排序，后对小写字母排序
sayings = ['cat', 'Tom', 'Angela', 'pet']
sayings.sort()
print("区分大小写排序：", sayings)
sayings.sort(key=str.lower)
print("不区分大小写排序：", sayings)
# 也可以使用内置的函数sorted()对列表进行排序，语法：sorted(iterable,key=None,reverse=False)
sayings_asc = sorted(sayings)
print(sayings, "升序排列：" + str(sayings_asc))
saying_desc = sorted(sayings, reverse=True)
print(sayings, "降序排列：" + str(saying_desc))
# listname.sort()函数 和 内置函数sorted(listname) 的区别：listname.sort()会改变列表中元素的顺序，而sorted(listname)则不会

# 列表推导式，使用列表推导式可以快速生成一个列表
# 1、生成指定范围的列表，语法：list=[Expression for var in range]
# 生成10个10~100范围内的随机数
import random

randoms = [random.randint(10, 100) for i in range(10)]
print(randoms)
# 2、根据原列表生成指定需求的列表，语法：list=[Expression for var in list]
half_randoms = [int(x * 0.5) for x in randoms]
print(half_randoms)
# 3、从列表中选择符合条件的元素组成新列表，语法：list=[Expression for var in list if condition]
bigger_randoms = [x for x in randoms if x >= 50]
print(bigger_randoms)

# 二维列表
# 1、直接定义二维列表，语法：listname=[[element1,element2],[element1,element2]]
rooms = [[1001, 1002, 1003], [2001, 2002, 2003]]
print(rooms)
# 2、使用嵌套for循环创建
houses = []
for i in range(2):
    houses.append([])
    for j in range(3):
        houses[i].append((i + 1) * 1000 + j + 1)
print(houses)
# 3、使用列表推导式创建
buildings = [[(i + 1) * 1000 + j + 1 for j in range(3)] for i in range(2)]
print(buildings)
# 访问二维列表中的元素，语法：listname[下标1][下标2]
print(buildings[0][1])

# 古诗横版排列和竖版排列
sentance1 = "春眠不觉晓"
sentance2 = "处处闻啼鸟"
sentance3 = "夜来风雨声"
sentance4 = "花落知多少"
sentances = [list(sentance1), list(sentance2), list(sentance3), list(sentance4)]
print("--------横版--------")
for i in range(4):
    for j in range(5):
        if j == 4:
            print(sentances[i][j])
        else:
            print(sentances[i][j], end="")
print("--------竖版--------")
sentances.reverse()
for i in range(5):
    for j in range(4):
        if j == 3:
            print(sentances[j][i])
        else:
            print(sentances[j][i], end="")
