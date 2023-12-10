def parse_winning_nums(s: str) -> set[int]:
    winning_nums = set()
    nums = s.strip().split(" ")
    for num in nums:
        if len(num) > 0:
            winning_nums.add(int(num.strip()))

    return winning_nums


def parse_nums(nums: str) -> list[int]:
    nums = nums.strip().split(" ")
    nums = [int(num.strip()) for num in nums if len(num) > 0]
    return nums


def parse_line(line: str) -> tuple[list[int], set[int]]:
    line = line[line.find(":") + 1 :]
    bar_idx = line.find("|")
    winning_nums = line[:bar_idx]
    nums = line[bar_idx + 1 :]

    return parse_nums(nums), parse_winning_nums(winning_nums)


def calculate_point_with_winning_nums(nums: list[int], winning_nums: set[int]) -> int:
    wins = 0
    for num in nums:
        if num in winning_nums:
            if wins == 0:
                wins = 1
            else:
                wins *= 2
    return wins


def calculate_card_points(line: str) -> int:
    nums, winning_nums = parse_line(line)
    return calculate_point_with_winning_nums(nums, winning_nums)


def calculate_all_card_points(lines: list[str]) -> int:
    points = 0
    for line in lines:
        points += calculate_card_points(line)
    return points


def calculate_cards_with_winning_nums(nums: list[int], winning_nums: set[int]) -> int:
    wins = 0
    for num in nums:
        if num in winning_nums:
            wins += 1

    return wins


def calculate_all_card_nums(lines: list[str]) -> int:
    copies = [1] * len(lines)
    for i, line in enumerate(lines):
        nums, winning_nums = parse_line(line)
        wins = calculate_cards_with_winning_nums(nums, winning_nums)

        for j in range(i + 1, i + 1 + wins):
            copies[j] += copies[i]

    return sum(copies)


if __name__ == "__main__":
    with open("example.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        points = calculate_all_card_points(lines)

        print(f"Sum of points: {points}")

        cards = calculate_all_card_nums(lines)
        print(f"Total no. of cards: {cards}")
