def explore_number(lines: list[str], i: int, j: int, visited: set[int]) -> int:
    if i < 0 or i >= len(lines):
        return 0
    if j < 0 or j >= len(lines[i]):
        return 0
    if not lines[i][j].isdigit():
        return 0
    if i * len(lines[i]) + j in visited:
        return 0

    line = lines[i]
    start, end = j, j
    while start > 0 and line[start - 1].isdigit():
        start -= 1
    while end < len(line) - 1 and line[end + 1].isdigit():
        end += 1

    for offset in range(start, end + 1):
        index = i * len(line) + offset
        visited.add(index)

    return int(line[start : end + 1])


def explore(lines: list[str]) -> int:
    total_sum = 0

    neighbors = [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]

    visited = set()
    for i, line in enumerate(lines):
        for j, symbol in enumerate(line):
            if not symbol.isdigit() and not symbol == "." and not symbol == "\n":
                print(symbol)
                for di, dj in neighbors:
                    total_sum += explore_number(lines, i + di, j + dj, visited)

    return total_sum


def explore_gear(lines: list[str]) -> int:
    total_sum = 0

    neighbors = [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]

    visited = set()
    for i, line in enumerate(lines):
        for j, symbol in enumerate(line):
            if symbol == "*":
                adj_nums = []
                for di, dj in neighbors:
                    num = explore_number(lines, i + di, j + dj, visited)
                    if num != 0:
                        adj_nums.append(num)

                if len(adj_nums) > 2:
                    raise Exception("More than two numbers found near gear...")
                if len(adj_nums) == 2:
                    total_sum += adj_nums[0] * adj_nums[1]

    return total_sum


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = f.readlines()
        total_sum = explore_gear(lines)
        print(f"Total sum: {total_sum}")

        # first 538217
