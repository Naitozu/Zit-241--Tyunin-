import numpy as np

# Ввод размеров матрицы
N = int(input("Введите количество строк (N): "))
M = int(input("Введите количество столбцов (M): "))

# Генерация случайной матрицы (можно заменить на ввод вручную)
B = np.random.randint(-20, 30, (N, M))
print("\nИсходная матрица B:")
print(B)

# Обработка каждой строки
for i in range(N):
    row = B[i]
    max_idx = np.argmax(row)  # Индекс максимального элемента
    min_idx = np.argmin(row)  # Индекс минимального элемента

    # Меняем местами max с первым элементом строки
    row[0], row[max_idx] = row[max_idx], row[0]

    # Меняем местами min с последним элементом строки
    row[-1], row[min_idx] = row[min_idx], row[-1]

print("\nИзмененная матрица B:")
print(B)
