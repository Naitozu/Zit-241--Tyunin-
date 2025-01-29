def process_array():


    n = int(input("Введите количество элементов массива: "))
    print(f"Введите {n} целых чисел через пробел:")
    array = list(map(int, input().split()))

    if len(array) != n:
        print("Ошибка: количество введенных элементов не совпадает с N.")
        return

    max_element = max(array)

    reversed_array = array[::-1]

    print("Максимальный элемент массива:", max_element)
    print("Массив в обратном порядке:", reversed_array)

process_array()
