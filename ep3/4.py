# 定义月份数字与英文缩写的对应关系
month_abbr = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# 从键盘输入一个表示月份的数字
month_num = int(input("请输入一个表示月份的数字(1~12): "))

# 检查输入的数字是否在有效范围内
if 1 <= month_num <= 12:
    # 输出对应月份的英文缩写
    print("对应月份的英文缩写为:", month_abbr[month_num - 1])
else:
    print("输入的数字不在有效范围内，请输入1到12之间的数字。")