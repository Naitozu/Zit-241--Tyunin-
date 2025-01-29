import math

def main():
    while True:
        print("\nВыберите фигуру для вычисления площади:")
        print("1. Круг")
        print("2. Прямоугольник")
        print("3. Треугольник")
        print("4. Квадрат")
        print("0. Выход")
        
        choice = input("Введите номер: ")
        
        if choice == "0":
            print("Программа завершена.")
            break
        
        if choice not in ("1", "2", "3", "4"):
            print("Ошибка: выберите вариант из списка (0-4).")
            continue
        
        # Обработка выбора
        if choice == "1":
        
            try:
                radius = float(input("Введите радиус круга: "))
                if radius <= 0:
                    raise ValueError
                area = math.pi * radius ** 2
                print(f"Площадь круга: {area:.2f}")
            except ValueError:
                print("Ошибка: радиус должен быть положительным числом.")
        
        elif choice == "2":
         
            try:
                length = float(input("Введите длину: "))
                width = float(input("Введите ширину: "))
                if length <= 0 or width <= 0:
                    raise ValueError
                area = length * width
                print(f"Площадь прямоугольника: {area:.2f}")
            except ValueError:
                print("Ошибка: длина и ширина должны быть положительными числами.")
        
        elif choice == "3":
         
            try:
                base = float(input("Введите основание: "))
                height = float(input("Введите высоту: "))
                if base <= 0 or height <= 0:
                    raise ValueError
                area = (base * height) / 2
                print(f"Площадь треугольника: {area:.2f}")
            except ValueError:
                print("Ошибка: основание и высота должны быть положительными числами.")
        
        elif choice == "4":

            try:
                side = float(input("Введите сторону квадрата: "))
                if side <= 0:
                    raise ValueError
                area = side ** 2
                print(f"Площадь квадрата: {area:.2f}")
            except ValueError:
                print("Ошибка: сторона должна быть положительным числом.")

if __name__ == "__main__":
    main()