def move_circle(lines: list[list[str]]) -> None: 
    move_north(lines)
    move_west(lines)
    move_south(lines)
    move_east(lines)

def move_north(lines: list[list[str]]) -> None:
    for j in range(len(lines[0])):
        i, available = 0, 0
        while i < len(lines):
            if lines[i][j] == "O":
                lines[available][j] = "O"
                if i != available:
                    lines[i][j] = "."

                available += 1
            elif lines[i][j] == "#":
                available = i + 1
            # print(available)
            i += 1


def move_west(lines: list[list[str]]) -> None:
    for i, line in enumerate(lines):
        j, available = 0, 0
        while j < len(line):
            if lines[i][j] == "O":
                lines[i][available] = "O"
                if j != available:
                    lines[i][j] = "."

                available += 1
            elif lines[i][j] == "#":
                available = j + 1
            j += 1

def move_south(lines: list[list[str]]) -> None:
    for j in range(len(lines[0])):
        i, available = len(lines) - 1, len(lines) - 1
        while i >= 0: 
            if lines[i][j] == "O":
                lines[available][j] = "O"
                if i != available:
                    lines[i][j] = "."

                available -= 1
            elif lines[i][j] == "#":
                available = i - 1
            # print(available)
            i -= 1

def to_tuple(lines: list[list[str]]) -> tuple[str]:
    return tuple(["".join(line) for line in lines])

def move_east(lines: list[list[str]]) -> None:
    for i, line in enumerate(lines):
        j, available = len(line) - 1, len(line) - 1
        while j >= 0: 
            if lines[i][j] == "O":
                lines[i][available] = "O"
                if j != available:
                    lines[i][j] = "."

                available -= 1
            elif lines[i][j] == "#":
                available = j - 1
            j -= 1

def score_pattern(lines: list[list[str]]) -> int:
    total_score = 0
    for j in range(len(lines[0])):
        for i in range(len(lines)): 
            if lines[i][j] == "O": 
                total_score += len(lines) - i
    return total_score

def map_to_nearest_circle(lines: list[list[str]], target_cycle: int) -> int:
    lines = [line[:] for line in lines]
    seens = {}
    i = 0
    while to_tuple(lines) not in seens:
        seens[to_tuple(lines)] = i
        move_circle(lines)
        i += 1

    print(f"Seen {i} in {seens[to_tuple(lines)]}")
    offset = seens[to_tuple(lines)]
    len_circle = i - seens[to_tuple(lines)]

    
    nearest_cycle = target_cycle - offset
    nearest_cycle %= len_circle
    nearest_cycle += offset
    return nearest_cycle

def move_multi_cycle(lines: list[list[str]], num_cycle: int) -> None:
    nearest_cycle = map_to_nearest_circle(lines, num_cycle)
    print(f"nearest cycle: {nearest_cycle}")
    for _ in range(nearest_cycle):
        move_circle(lines)

if __name__ == "__main__":
    with open("input.txt", "r", encoding="utf-8") as f:
        lines = [list(line.strip()) for line in f]
        move_north(lines)
        score = score_pattern(lines)

        print(f"Score: {score}")

        move_multi_cycle(lines, 1_000_000_000)
        print(f"part 2 score: {score_pattern(lines)}")
         