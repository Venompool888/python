import math

# 从键盘输入三角形的三条边长
a = float(input("请输入三角形的第一条边长: "))
b = float(input("请输入三角形的第二条边长: "))
c = float(input("请输入三角形的第三条边长: "))

# 检查输入的边长是否能构成三角形
if a + b > c and a + c > b and b + c > a:
    # 使用海伦公式计算三角形的面积
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print("三角形的面积为:", area)
else:
    print("输入的边长不能构成三角形")