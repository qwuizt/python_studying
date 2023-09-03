a, b, c = 10, 9, 10
if a + b < c or b + c < a or a + c < b:
    print("Треугольник не существует")
elif a != b and a != c and b != c:
    print("Тругольник разносторонний")
elif a == b and a == c and b == c:
    print("Тругольник равносторонний")
else:
    print("Тругольник равнобедренный")
