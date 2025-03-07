# 初始里程数
initial_mileage = 23352
# 最终里程数
final_mileage = 23690
# 加油量（升）
fuel_consumed = 24

# 行驶的总里程
distance_traveled = final_mileage - initial_mileage
# 每百千米的平均油耗
average_fuel_consumption = (fuel_consumed / distance_traveled) * 100

print("每百千米的平均油耗为:", average_fuel_consumption, "升")