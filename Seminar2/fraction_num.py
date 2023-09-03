from fractions import Fraction

fraction1_str = input("Введите первую дробь в формате a/b: ")
fraction2_str = input("Введите вторую дробь в формате a/b: ")

numerator1_str, denominator1_str = fraction1_str.split('/')
numerator2_str, denominator2_str = fraction2_str.split('/')

numerator1, denominator1 = int(numerator1_str), int(denominator1_str)
numerator2, denominator2 = int(numerator2_str), int(denominator2_str)

sum_numerator = numerator1 * denominator2 + numerator2 * denominator1
sum_denominator = denominator1 * denominator2

multiplication_numerator = numerator1 * numerator2
multiplication_denominator = denominator1 * denominator2

for i in range(2, min(sum_numerator, sum_denominator) + 1):
    while (sum_numerator % i == 0) and (sum_denominator % i == 0):
        sum_numerator //= i
        sum_denominator //= i

for i in range(2, min(multiplication_numerator, multiplication_denominator) + 1):
    while (multiplication_numerator % i == 0) and (multiplication_denominator % i == 0):
        multiplication_numerator //= i
        multiplication_denominator //= i

print(f"Сумма дробей: {sum_numerator}/{sum_denominator}")
print(f"Произведение дробей: {multiplication_numerator}/{multiplication_denominator}")
print(f"Проверка суммы с помощью модуля fraction: {Fraction(fraction1_str) + Fraction(fraction2_str)}")
print(f"Проверка умножения с помощью модуля fraction: {Fraction(fraction1_str) * Fraction(fraction2_str)}")
