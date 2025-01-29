text = input().lower() 
words = text.split()
count = 0
for word in words:
    cleaned_word = word.strip('.,!?;:"\'()[]{}')
    if cleaned_word.startswith('е'):
        count += 1
print(count)