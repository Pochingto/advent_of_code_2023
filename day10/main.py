from collections import deque

DIRS = {
    "|": [[-1, 0], [1, 0]],
    "-": [[0, -1], [0, 1]],
    "L": [[-1, 0], [0, 1]],
    "J": [[-1, 0], [0, -1]],
    "7": [[1, 0], [0, -1]],
    "F": [[1, 0], [0, 1]],
}


def bfs(start: tuple[int, int], starting_dir: str, lines: list[str]) -> int:
    x, y = start
    dq = deque()
    visited = set()
    visited.add((x, y))
    for dx, dy in DIRS[starting_dir]:
        if x + dx < 0 or x + dx >= len(lines):
            continue
        if y + dy < 0 or y + dy >= len(lines[x]):
            continue
        dq.append((x + dx, y + dy))
        visited.add((x + dx, y + dy))

    steps = 0
    while dq:
        len_dq = len(dq)
        for _ in range(len_dq):
            x, y = dq.popleft()
            for dx, dy in DIRS[lines[x][y]]:
                if x + dx < 0 or x + dx >= len(lines):
                    continue
                if y + dy < 0 or y + dy >= len(lines[x]):
                    continue
                if (x + dx, y + dy) not in visited:
                    dq.append((x + dx, y + dy))
                    visited.add((x + dx, y + dy))

        steps += 1

    return steps, visited


def calculate_area(
    visited: set[tuple[int, int]], lines: list[str], starting_dir: str
) -> int:
    area = 0
    for x, line in enumerate(lines):
        north = 0
        south = 0
        for y, tile in enumerate(line):
            if tile == "S":
                tile = starting_dir

            if (x, y) in visited:
                if [-1, 0] in DIRS[tile]:
                    north += 1
                if [1, 0] in DIRS[tile]:
                    south += 1
            elif north % 2 == 1:
                try:
                    assert south % 2 == 1
                    area += 1
                except AssertionError as exc:
                    print(f"North, South {north, south}")
                    print(f"processing x y {x, y}")
                    print(f"tile {tile}")
                    raise AssertionError(
                        "North and south count not consistent"
                    ) from exc

    return area


def find_starting_xy(lines: list[str]) -> tuple[int, int]:
    for x, line in enumerate(lines):
        for y, tile in enumerate(line):
            if tile == "S":
                return x, y


if __name__ == "__main__":
    with open("input.txt", "r", encoding="utf-8") as f:
        STARTING_DIR = "L"
        lines = f.readlines()
        x, y = find_starting_xy(lines)
        print(f"STARTING X,Y: {x, y}")
        steps, visited = bfs((x, y), STARTING_DIR, lines)
        print(f"steps: {steps}")

        # lines[x][y] = STARTING_DIR
        area = calculate_area(visited, lines, STARTING_DIR)
        print(f"Area: {area}")
