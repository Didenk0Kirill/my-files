import random

first_name  = input("Введіть ваше ім'я: ")
last_name = input("Введіть ваше прізвище: ")

n = len(first_name)
m = len(last_name)

print(f"Розмір матриці: {m}x{n} (рядків: {m}, стовпців: {n}")

matrix_a = [[random.random() for _ in range(n)] for _ in range(m)]
matrix_b = [[random.randint(-10,10) for _ in range(n)] for _ in range(m)]
matrix_v = [[random.randint(0,20) for _ in range(n)] for _ in range(m)]
matrix_g = [[random.uniform(-10,10) for _ in range(n)] for _ in range(m)]

print("\nМатриця(в)")
for row in matrix_v:
    print(row)

max_val = matrix_v[0][0]
max_row_index = 0

for i in range(m):
    for j in range(n):
        if matrix_v[i][j] > max_val:
            max_val = matrix_v[i][j]
            max_row_index = 1

print(f"\nМаксимальний елемент {max_val} знаходиться в рядку {max_row_index}")

matrix_v[0], matrix_v[max_row_index] = matrix_v[max_row_index], matrix_v[0]

print("\nМатриця (в) після заміни першого рядка з рядком з макс. елементом:")
for row in matrix_v:
    print(row)