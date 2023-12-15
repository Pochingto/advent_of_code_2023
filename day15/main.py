def hash(string: str) -> int:
    current = 0
    for char in string:
        current += ord(char)
        current *= 17
        current %= 256

    return current


def parse_line(line: str) -> list[str]:
    return [string.strip() for string in line.strip().split(",")]


def calculate_sum_of_hash(strings: list[str]) -> int:
    return sum(map(hash, strings))


if __name__ == "__main__":
    with open("input.txt", "r", encoding="utf-8") as f:
        strings = parse_line(f.readline())

        # part 1
        sum_hash = calculate_sum_of_hash(strings)
        print(f"Sum of hash: {sum_hash}")
