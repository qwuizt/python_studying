# Использование метода count()

text = input("Введите строку текста: ")

frequency_dict1 = {}
for char in text:
    if char.isalpha():
        frequency_dict1[char] = text.count(char)

print(f"Результат с использованием метода count(): {frequency_dict1}")

# Без использования метода count()

frequency_dict2 = {}

for char in text:
    if char.isalpha():
        if char in frequency_dict2:
            frequency_dict2[char] += 1
        else:
            frequency_dict2[char] = 1

print(f"Результат без использования метода count(): {frequency_dict2}")
