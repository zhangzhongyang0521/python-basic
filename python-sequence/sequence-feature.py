# 序列是一块用于存放多个值的连续内存空间，并按照一定顺序排列，每个元素都有一个索引
# python中常见的序列：列表、元组、集合、字典和字符串

# 索引，python中的序列索引从0开始（从左到右），从-1开始（从右到左）
words = ["AA", "BB", "CC", "DD", "EE"]
print(words[2])
print(words[-1])

# 切片，访问序列中一定范围的元素，可以通过切片生成新的序列
# 语法格式：sname[start:end:step]，其中start如果不指定默认为0，end若不指定默认为序列的长度，step若不指定默认为1
print(words[1:3])
print(words[0:5:2])
# 复制整个列表时，可以同时省略start和end
copy_words = words[:]
print(copy_words == words)
print(copy_words)

# 序列相加，python中支持两种类型相同的序列相加（使用+号），不会去重元素。
# 相加的两个序列必须是同种类型（同为列表，元组、集合等），序列中的元素类型可以不相同
prices = [10.90, 21.86, 15.56]
names = ["python入门", "Java入门"]
print(prices + names)
# print(prices + "prices"),因是不同类型，会导致运行异常TypeError: can only concatenate list (not "str") to list

# 序列乘法，使用数字n乘以序列，会生成新的序列，新序列中重复n次原来的序列
print(prices * 2)
empty_list = [None] * 5
print(empty_list)

# 检查元素是否是序列的成员，语法结构 value in sequence
print(10.90 in prices)
print(18.88 in prices)
print(18.88 not in prices)

# 检查序列的长度（使用len()函数）、最大值（使用max()函数）和最小值（使用min()函数）
print(len(prices))
print(max(prices))
print(min(names))

# 序列的常用内置函数
# list() 将序列转为列表
price_list = list(prices)
print(type(prices), type(price_list))
# str() 将序列转为字符串
price_str = str(prices)
print(price_str)
print(type(prices), type(price_str))
# sum() 计算元素和
print(sum(prices))
# sorted() 对序列进行排序
print(sorted(prices))
# reversed() 反向序列中的元素
for price in reversed(prices):
    print(price, end=" ")
    print()
# enumerate() 将序列组合为组合为索引序列，常在for循环中用
for price in enumerate(prices):
    print(price, end=" ")
