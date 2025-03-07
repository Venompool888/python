# 定义汇率
usd_to_rmb_rate = 6.868
rmb_to_usd_rate = 0.1456

# 从键盘输入货币及对应的货币符号
amount = float(input("请输入货币的币值: "))
currency = input("请输入货币符号（USD 或 RMB）: ").strip().upper()

# 根据输入的货币符号进行转换
if currency == "USD":
    # 将美元转换为人民币
    converted_amount = amount * usd_to_rmb_rate
    print("转换后的人民币币值为: {:.2f} RMB".format(converted_amount))
elif currency == "RMB":
    # 将人民币转换为美元
    converted_amount = amount * rmb_to_usd_rate
    print("转换后的美元币值为: {:.2f} USD".format(converted_amount))
else:
    print("无效的货币符号，请输入 USD 或 RMB。")