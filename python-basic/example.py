# 模拟手机充值场景
money = int(input("欢迎使用手机充值，请输入需要充值的金额："))
print("已成功充值" + str(money))

# 打印石头怪
print(2 * ' ' + 5 * '*' + 2 * ' ')
print(' ' + '*' + 5 * ' ' + ' ' + '*')
print('*' + 2 * ' ' + '@' + 3 * ' ' + '@' + 2 * ' ' + '*')
print('*' + 7 * ' ' + '*')
print('*' + 3 * ' ' + '@' + 3 * ' ' + '*')
print('*' + 7 * ' ' + '*')
print(' ' + '*' + 5 * ' ' + ' ' + '*')

# 预测小孩身高
fatherHeight = float(input("父亲身高:"))
motherHeight = float(input("母亲身高:"))
print("你们的孩子身高可能为：" + str((fatherHeight + motherHeight) * 0.54))

# 根据总步数计算消耗的热量值
totalSteps = int(input("输入当天的总步数:"))
print("今天总共消耗:" + str(totalSteps * 28))
