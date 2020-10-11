# 模拟支付宝蚂蚁森林的能量产生过程
flag = False
while not flag:
    print("查询能量请输入来源！退出程序请输入0")
    print("能量来源如下：")
    print("生活缴费、行走捐、线下支付")
    source = input("")
    if source == "生活缴费":
        print("能量为：", 100)
    elif source == "行走捐":
        print("能量为：", 200)
    elif source == "线下支付":
        print("能量为：", 300)
    elif source == "0":
        flag = True
        print("已退出")

# 猜数字游戏
print("--------猜数字游戏--------")
print("请输入1~10之间的任意一个数：")
match = False
while not match:
    value = int(input(""))
    if value < 9:
        print("太小，请重新输入")
    elif value > 9:
        print("太大，请重新输入")
    elif value == 9:
        match = True
        print("恭喜你，猜中了")

# 模拟“跳一跳”小游戏的加分块
print("---------跳一跳---------")
print("欢迎回来，请开始游戏")
print("请输入（中心、音乐块、微信支付块），结束请输入0")
flag = False
while not flag:
    position = input("请输入:")
    if position == "中心":
        print("加2分")
    elif position == "音乐块":
        print("加30分")
    elif position == "微信支付块":
        print("加50分")
    elif position == "0":
        flag = True
        print("已退出")

# 模拟10086查询功能
print("--------10086查询功能--------")
print("输入1，查余额")
print("输入2，查流量")
print("输入3，查剩余通话时长")
print("输入0，退出")
while True:
    option = int(input(""))
    if option == 1:
        print("当前余额：999元")
    elif option == 2:
        print("当前剩余流量：5G")
    elif option == 3:
        print("当前剩余通话时长：180分钟")
    elif option == 0:
        print("已退出")
        break