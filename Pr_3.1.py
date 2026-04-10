import random

n = int(input("Введіть кількість елементів n: "))

list_a = [random.random() for _ in range(n)]
list_b = [random.randint(-10, 10) for _ in range(n)]
list_c = [random.randint(0, 50) for _ in range(n)]

print(f"Список (a): {list_a}")
print(f"Список (б): {list_b}")
print(f"Список (в): {list_c}")
print("-" * 30)
is_decreasing = True
for i in range(len(list_b) - 1):
    if list_b[i] <= list_b[i+1]:
        is_decreasing = False
        break

new_list = list_b.copy()
if not is_decreasing:
    for i in range(len(new_list)):
        if new_list[i] < 0:
            new_list[i] = 1
    print("Послідовність не спадна. Від'ємні елементи замінено на 1")
else:
    print("Послідовність спадна. Змін не проведено")

print(f"Результат: {new_list}")