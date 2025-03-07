import math

# 从键盘输入球的半径
radius = float(input("请输入球的半径: "))

# 计算球的表面积
surface_area = 4 * math.pi * radius ** 2

# 计算球的体积
volume = (4 / 3) * math.pi * radius ** 3

print("球的表面积为:", surface_area)
print("球的体积为:", volume)