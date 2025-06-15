import requests
from collections import Counter
import string

def get_reference_text():
    """Получает эталонный текст с fish-text.ru"""
    url = "https://fish-text.ru/get"
    params = {
        'type': 'paragraph',
        'number': 50,  
        'format': 'json'
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data.get('text', '')
    return ""

def build_frequency_dict(text):
    """Строит частотный словарь букв (только русские буквы)"""
    russian_letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    letters = [char.lower() for char in text if char.lower() in russian_letters]
    total_letters = len(letters)
    if total_letters == 0:
        return {}
    
    freq = Counter(letters)

    return {char: (count / total_letters) * 100 for char, count in freq.items()}

def caesar_decrypt(ciphertext, shift):
    """Дешифрует текст шифром Цезаря"""
    decrypted = []
    for char in ciphertext:
        if 'а' <= char.lower() <= 'я':
            is_upper = char.isupper()
            char_code = ord(char.lower())

            shifted_code = (char_code - ord('а') - shift) % 33 + ord('а')
            decrypted_char = chr(shifted_code)
            if is_upper:
                decrypted_char = decrypted_char.upper()
            decrypted.append(decrypted_char)
        else:
            decrypted.append(char)
    return ''.join(decrypted)

def find_best_shift(ciphertext, ref_freq):
    """Находит оптимальный сдвиг по частотному анализу"""
    cipher_freq = build_frequency_dict(ciphertext)
    if not cipher_freq or not ref_freq:
        return 0
    
    best_shift = 0
    min_error = float('inf')
    
    for shift in range(33):
        error = 0
        for cipher_char, cipher_percent in cipher_freq.items():
            orig_code = (ord(cipher_char) - ord('а') - shift) % 33 + ord('а')
            orig_char = chr(orig_code)
            ref_percent = ref_freq.get(orig_char, 0)
            error += abs(cipher_percent - ref_percent)
        
        if error < min_error:
            min_error = error
            best_shift = shift
    
    return best_shift

def main():
    print("Получаем эталонный текст с fish-text.ru...")
    reference_text = get_reference_text()
    
    if not reference_text:
        print("Не удалось получить эталонный текст")
        return
    
    print(f"Получено {len(reference_text)} символов")
    
    ref_freq = build_frequency_dict(reference_text)
    
    ciphertext = input("Введите зашифрованный текст: ")
    
    best_shift = find_best_shift(ciphertext, ref_freq)
    print(f"Найденный сдвиг: {best_shift}")
    
    decrypted = caesar_decrypt(ciphertext, best_shift)
    print("\nРезультат расшифровки:")
    print(decrypted)

if __name__ == "__main__":
    main()