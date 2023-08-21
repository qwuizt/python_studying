START_RANGE = 0
END_RANGE = 100 * 10 ** 3
while True:
    num = int(input("Введите число: "))
    if START_RANGE <= num <= END_RANGE:
        if num == 0 or num == 1:
            print(f"{num} - ни простое, ни систавное число")
            break
        else:
            k = 0
            for i in range(2, num // 2 + 1):
                if num % i == 0:
                    k = k + 1
            if k == 0:
                print("Число - простое")
                break
            else:
                print("Число - составное")
                break
    else:
        print("Введите число больше 0 и меньше 100 тыс.")
