names = ["Alex", "Maria", "Ivan"]
rates = [10000, 15000, 20000]
bonuses = ["10.25%", "15.5%", "12.75%"]

result_dict = {name: rate * float(bonus[:-1]) / 100 for name, rate, bonus in
               zip(names, rates, bonuses)}

print(result_dict)
