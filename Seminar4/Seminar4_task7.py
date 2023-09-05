my_dict = {
    "Компания A": [1000, -1000, -300],
    "Компания B": [500, 100, 50],
    "Компания C": [800, -100, -200]
}


def calculate_profit(company_data):
    total_profit = []
    for financial_data in company_data.values():
        total_profit.append(sum(financial_data))
    print(total_profit)
    for income in total_profit:
        if income < 0:
            return False
    return True


result = calculate_profit(my_dict)
print(result)
