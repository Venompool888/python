# 从键盘输入一个三位整数
number = int(input("请输入一个三位整数: "))

# 检查输入是否为三位数
if 100 <= number <= 999 or -999 <= number <= -100:
    # 将整数转换为字符串并反转
    reversed_number = int(str(number)[::-1]) if number > 0 else -int(str(abs(number))[::-1])
    print("反序数为:", reversed_number)
else:
    print("输入的不是一个三位整数")