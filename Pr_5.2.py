import math
def taylor_exp_custom(x, epsilon):
    u = 1+x
    term = 1.0
    current_sum = term
    n = 1

    while True:
        term *= u / n
        current_sum +=term
        if abs(term) <= epsilon:
            break
        n += 1
        if n > 500:
            break
    return current_sum, n

def main():
    try:
        a = float(input("Введіть початок відрізка а: "))
        b = float(input("Введіть початок відрізка б: "))
        eps = float(input("Введіть точність epsilon(наприклад 0.0001): "))
    except ValueError:
        print("Помилка: треба ввести число")
        return

    m = 10
    step = (b - a) / (m -1)

    header = f"{'xi' :>10} | {'f(xi)точне':>15} | {'f(xi) наближ.':>10}"
    print("-" * len(header))
    print(header)
    print("-" * len(header))

    for i in range(m):
        xi = a + i * step
        exact_val = math.exp(1 + xi)
        approx_val, iteration = taylor_exp_custom(xi, eps)
        print(f"{xi:10.4f} | {exact_val:15.6f} | {approx_val:15.6f} | {eps:10} | {iteration:10}")

if __name__ == "__main__":
    main()
