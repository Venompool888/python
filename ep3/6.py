# 定义美元兑换人民币的汇率
exchange_rate = 6.868

# 从键盘输入美元的币值
usd = float(input("请输入美元的币值: "))

# 将美元转换为人民币
rmb = usd * exchange_rate

# 输出转换后的人民币币值，保留2位小数
print("转换后的人民币币值为: {:.2f}".format(rmb))