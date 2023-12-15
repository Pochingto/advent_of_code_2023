def hash(string: str) -> int:
    current = 0
    for char in string:
        current += ord(char)
        current *= 17
        current %= 256

    return current


def part2_hash_map(strings: str) -> list[list[tuple[str, int]]]:
    boxes = [[] for _ in range(256)]

    for string in strings:
        op_idx = string.find("=")
        if op_idx == -1:
            op_idx = string.find("-")

        label, op = string[:op_idx], string[op_idx]
        box_idx = hash(label)
        if op == "-":
            for l, f in boxes[box_idx]:
                if l == label:
                    boxes[box_idx].remove((l, f))
        elif op == "=":
            focal = int(string[-1])
            exists = False
            for i, (l, f) in enumerate(boxes[box_idx]):
                if l == label:
                    boxes[box_idx][i] = (label, focal)
                    exists = True
                    break
            if not exists:
                boxes[box_idx].append((label, focal))

    return boxes


def calculate_focal_power(boxes: list[list[tuple[str, int]]]) -> int:
    focal_power = 0
    for i, box in enumerate(boxes):
        for j, (_, focal) in enumerate(box):
            focal_power += (i + 1) * (j + 1) * focal

    return focal_power


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

        # part2
        boxes = part2_hash_map(strings)
        focal_power = calculate_focal_power(boxes)
        print(f"focal power: {focal_power}")
