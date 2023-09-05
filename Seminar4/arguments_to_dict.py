def arguments_to_dict(**kwargs):
    argument_map = {}
    for key, value in kwargs.items():
        if isinstance(key, (int, float, str)):
            argument_map[value] = key
        else:
            argument_map[str(key)] = value
    return argument_map


result = arguments_to_dict(name="John", age=30, salary=50000, owns=("house", "flat"))
print(result)
