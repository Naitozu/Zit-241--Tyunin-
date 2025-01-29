def get_array(index):
    while True:
        try:
            arr = list(map(int, input(f"Введите элементы {index}-го массива через пробел (не более 15): ").split()))
            if len(arr) > 15:
                print("Ошибка: размер массива не должен превышать 15 элементов.")
                continue
            return arr
        except ValueError:
            print("Ошибка: Введите только целые числа через пробел.")


def calculate_sum_and_average(arr):
    total = sum(arr)
    avg = total / len(arr) if arr else 0
    return total, avg


def main():
    arrays = [get_array(i + 1) for i in range(3)]
    
    for i, arr in enumerate(arrays, start=1):
        total, avg = calculate_sum_and_average(arr)
        print(f"Массив {i}: Сумма = {total}, Среднее арифметическое = {avg:.2f}")


if __name__ == "__main__":
    main()