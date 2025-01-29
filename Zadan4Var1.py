def print_numbers(a, b):

    if a > b:
        print("Ошибка: A должно быть меньше или равно B.")
        return
    for num in range(a, b + 1):
        print(num)


print_numbers(0, 9)
