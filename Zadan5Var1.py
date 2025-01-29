n = int(input())
current = 1
result = []
while current ** 2 <= n:
    result.append(str(current ** 2))
    current += 1
print(' '.join(result))