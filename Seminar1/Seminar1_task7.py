START_RANGE = 1
END_RANGE = 999
while True:
    num = int(input("Введите число от 1 до 999: "))
    if START_RANGE <= num <= END_RANGE:
        if num // 10 == 0:
            print(f"Ваше число - это цифра, {num} \n ее квадрат: {num ** 2}")
        elif num // 100 == 0:
            print(f"Ваше число - двузначное,\n произведение цифр числа: {(num // 10) * (num % 10)}")
        else:
            print(f"Ваше число - трёхзначное, \n зеркальное отображение:"
                  f"{num % 10 * 100 + num % 100 // 10 * 10 + num // 100}")
        break
    else:
        print("вы ввели число не из диапазона")
