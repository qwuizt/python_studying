import operator

MAX_CAPACITY = 10

items = {
    "спальник": 2,
    "еда": 5,
    "палатка": 7,
    "фонарик": 1,
    "карта": 3,
}

fit_in_backpack = []
sorted_items = sorted(items.items(), key=operator.itemgetter(1), reverse=True)

current_capacity = 0
for item in sorted_items:
    item_name, item_weight = item
    if current_capacity + item_weight <= MAX_CAPACITY:
        fit_in_backpack.append(item)
        current_capacity += item_weight

print("Вещи, которые влезут в рюкзак:")
for item_name, item_weight in fit_in_backpack:
    print(f"{item_name}: {item_weight} kg")
