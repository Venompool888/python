# 从键盘输入自己和室友的中文名
names = []
for i in range(3):
    name = input(f"请输入第{i+1}个名字: ")
    names.append(name)

# 取出所有名字的最后一个字并拼在一起
combined_name = ''.join([name[-1] for name in names])

# 输出宿舍的组合名
print("宿舍的组合名为:", combined_name)