rows = int(input('Сколько рядов у елки?: '))
count = 0
for i in range(1, rows + 1):
    columns = rows - i
    print(columns * ' ' + (i + count) * '*')
    count += 1
