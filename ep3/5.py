# 定义人民币兑换美元的汇率
exchange_rate = 0.1456

# 从键盘输入人民币的币值
rmb = float(input("请输入人民币的币值: "))

# 将人民币转换为美元
usd = rmb * exchange_rate

# 输出转换后的美元币值，保留2位小数
print("转换后的美元币值为: {:.2f}".format(usd))