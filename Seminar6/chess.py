import random


def random_queens_placement():
    queens = [(i, random.randint(1, 8)) for i in range(8)]
    return queens


def are_queens_safe(queens):
    for i in range(7):
        for j in range(i+1, 8):
            if queens[i][0] == queens[j][0] or queens[i][1] == queens[j][1] or abs(queens[i][0] - queens[j][0]) == abs(queens[i][1] - queens[j][1]):
                return False
    return True


def find_successful_placements(count):
    successful_placements = []
    attempts = 0
    while len(successful_placements) < count and attempts < 1000000:
        queens = random_queens_placement()
        if are_queens_safe(queens):
            successful_placements.append(queens)
        attempts += 1
    return successful_placements


if __name__ == "__main__":
    successful_placements = find_successful_placements(4)
    for i, placement in enumerate(successful_placements, start=1):
        print(f"Successful Placement {i}:")
        for x, y in placement:
            print(f"Queen at ({x}, {y})")
        print()


