import logging
import argparse

WEALTH_TAX_THRESHOLD = 5000000
WITHDRAWAL_PERCENTAGE = 0.015
MIN_WITHDRAWAL_FEE = 30
MAX_WITHDRAWAL_FEE = 600
INTEREST_RATE = 0.03
WEALTH_TAX_RATE = 0.10
DEPOSIT_INCREMENT = 50

balance = 0
transactions = []
operations_count = 0

logging.basicConfig(filename='ATM_app.log', level=logging.ERROR)


def deposit(amount):
    global balance, transactions, operations_count
    if amount % DEPOSIT_INCREMENT != 0 or amount <= 0:
        logging.error(f"Сумма пополнения должна быть кратной {DEPOSIT_INCREMENT} у.е. и больше 0")
        return

    balance += amount
    operations_count += 1
    if operations_count % 3 == 0:
        charge_interest()
    transactions.append(("Пополнение", amount))
    print("Операция выполнена.")
    print_balance()


def withdraw(amount):
    global balance, transactions, operations_count
    if amount % DEPOSIT_INCREMENT != 0 or amount <= 0:
        logging.error(f"Сумма снятия должна быть кратной {DEPOSIT_INCREMENT} у.е.")
        return

    if balance < amount:
        logging.error("Недостаточно средств на счете")
        return

    if balance > WEALTH_TAX_THRESHOLD:
        charge_wealth_tax()

    withdrawal_fee = max(MIN_WITHDRAWAL_FEE, min(MAX_WITHDRAWAL_FEE, amount * WITHDRAWAL_PERCENTAGE))
    balance -= (amount + withdrawal_fee)
    operations_count += 1
    if operations_count % 3 == 0:
        charge_interest()
    transactions.append(("Снятие", amount))
    print("Операция выполнена.")
    print_balance()


def charge_interest():
    global balance
    interest = INTEREST_RATE * balance
    balance -= interest


def charge_wealth_tax():
    global balance
    wealth_tax = WEALTH_TAX_RATE * balance
    balance -= wealth_tax


def print_balance():
    global balance
    print(f"Баланс: {balance} у.е.")


def print_transactions():
    global transactions
    print("Список операций:")
    for operation, amount in transactions:
        print(f"{operation}: {amount} у.е.")


def main():
    while True:
        print("Доступные действия:")
        print("1. Пополнить")
        print("2. Снять")
        print("3. Вывести баланс")
        print("4. Вывести список операций")
        print("5. Выйти")
        choice = input("Выберите действие (1/2/3/4/5): ")

        if choice == '1':
            amount = int(input(f"Введите сумму для пополнения (кратную {DEPOSIT_INCREMENT} у.е.): "))
            deposit(amount)
        elif choice == '2':
            amount = int(input(f"Введите сумму для снятия (кратную {DEPOSIT_INCREMENT} у.е.): "))
            withdraw(amount)
        elif choice == '3':
            print_balance()
        elif choice == '4':
            print_transactions()
        elif choice == '5':
            break
        else:
            logging.error("Неверный выбор. Пожалуйста, выберите 1, 2, 3, 4 или 5.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ATM Application")
    parser.add_argument('--amount', type=int, help='Amount for deposit or withdrawal')
    args = parser.parse_args()

    if args.amount:
        deposit(args.amount)
    else:
        main()
