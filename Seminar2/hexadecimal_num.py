
def decimal_to_hexadecimal(decimal_num):
    hex_digits = "0123456789ABCDEF"
    hex_representation = ""
    if decimal_num == 0:
        return "0"
    while decimal_num > 0:
        remainder = decimal_num % 16
        hex_representation = hex_digits[remainder] + hex_representation
        decimal_num //= 16

    return hex_representation


num = int(input("Введите целое число: "))
hex_result = decimal_to_hexadecimal(num)
print(f"Шестнадцатеричное представление числа {num}: {hex_result}")
print(f"Проверка программы: {hex(num)}")
