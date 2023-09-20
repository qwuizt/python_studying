from sys import argv


def _leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False


def exist_date(date_str):
    try:
        day, month, year = map(int, date_str.split('.'))
        if year < 1 or year > 9999:
            return False

        if month < 1 or month > 12:
            return False

        if month in [1, 3, 5, 7, 8, 10, 12]:
            if day < 1 or day > 31:
                return False
        elif month in [4, 6, 9, 11]:
            if day < 1 or day > 30:
                return False
        elif month == 2:
            if _leap_year(year):
                if day < 1 or day > 29:
                    return False
            else:
                if day < 1 or day > 28:
                    return False
        else:
            return False
        return True

    except ValueError:
        return False


if __name__ == "__main__":
    date_str = argv[1]
    if exist_date(date_str):
        print(f"{date_str} - дата существует")
    else:
        print(f"{date_str} - дата не существует")