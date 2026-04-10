import math

x = 0.1
x_max = 1.2
delta_x = 0.1

print(f"{'x':>5} | {'y':>10}")
print("-" * 18)

while x <= x_max + delta_x / 2:
    denominator = x**3+7.5
    if denominator != 0:
        y = math.tan(0.5 * x) / denominator
        print(f"{x:5.1f} | {y:10.6f}")
    else:
        print(f"{x:5.1f} | Помилка: ділення на 0")
    x += delta_x