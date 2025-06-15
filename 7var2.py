s = input("Введите строку: ")

upper_count = sum(1 for char in s if char.isupper())
lower_count = sum(1 for char in s if char.islower())

if upper_count > lower_count:
    result = s.upper()
elif lower_count > upper_count:
    result = s.lower()
else:
    result = s.lower()

print("Результат:", result)