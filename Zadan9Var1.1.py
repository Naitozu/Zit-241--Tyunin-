import numpy as np

# Ввод размерности матрицы
N = int(input("Введите размер N квадратной матрицы: "))

# Генерация случайной матрицы N x N (можно заменить на ввод вручную)
A = np.random.randint(-10, 20, (N, N))  
print("Матрица A:")
print(A)

# Вычисление суммы и количества положительных элементов над главной диагональю
positive_sum = 0
positive_count = 0

for i in range(N):
    for j in range(i + 1, N):  # Только над главной диагональю
        if A[i, j] > 0:
            positive_sum += A[i, j]
            positive_count += 1

print(f"\nСумма положительных элементов над главной диагональю: {positive_sum}")
print(f"Число положительных элементов: {positive_count}")
