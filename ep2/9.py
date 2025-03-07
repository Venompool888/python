# 初始武力值
initial_power = 1.0

# 每天增加或减少的百分比
increase_rate = 0.01
decrease_rate = 0.01

# 计算天天向上的武力值
up_power = initial_power
for _ in range(365):
    up_power *= (1 + increase_rate)

# 计算天天向下的武力值
down_power = initial_power
for _ in range(365):
    down_power *= (1 - decrease_rate)

print("天天向上的武力值为:", up_power)
print("天天向下的武力值为:", down_power)