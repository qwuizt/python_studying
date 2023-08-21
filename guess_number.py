from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
ATTEMPT_COUNT = 10

num = randint(LOWER_LIMIT, UPPER_LIMIT)
while True:
    tries = 0
    for i in range(1, ATTEMPT_COUNT + 1):
        guess = int(input(f"попытка {i}. Введите число: "))
        if guess < num:
            print("Загаданное число больше")
        elif guess > num:
            print("Загаданное число меньше")
        else:
            print(f"Вы угадали число {num} за {i} попыток")
            break
        if tries == 10:
            print(f"У вас закончились попытки. Загаданное число было {num}")
