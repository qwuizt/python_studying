class Person:
    max_up = 3

    def __init__(self, name, race='unknown'):
        self.name = name
        self.race = race
        self.level = 1
        self.health = 100

    def level_up(self):
        self.level += 1

    def change_health(self, quantity):
        try:
            choose = str(input())
            if choose == "-":
                self.health -= quantity
            if choose == "+":
                self.health += quantity
        except ValueError:
                return "False"


p2 = Person('Иван', 'Человек')
p1 = Person('Сильвана', 'Эльф')

p3 = Person('Грогу')
print(f'{p1.health = }, {p2.health = }, {p3.health = }')
p2.change_health(10)
print(f'{p1.health = }, {p2.health = }, {p3.health = }')
