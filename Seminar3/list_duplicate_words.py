
input_list = [1, 2, 2, 3, 4, 4, 4, 5, 6, 6]

duplicates_list = []

unique_elements = []

for item in input_list:
    if item not in unique_elements:
        unique_elements.append(item)
    else:
        if item not in duplicates_list:
            duplicates_list.append(item)

print(duplicates_list)
