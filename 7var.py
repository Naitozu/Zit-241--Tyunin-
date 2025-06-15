n = int(input("Введите число: "))
sqrt_n = n ** 0.5
lower = int(sqrt_n)
upper = lower + 1

if abs(lower ** 2 - n) <= abs(upper ** 2 - n):
    closest = lower
else:
    closest = upper

print(f"Число, квадрат которого ближе всего к {n}: {closest} (его квадрат: {closest ** 2})")