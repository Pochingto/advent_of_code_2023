def find_shortest_path(
    g1: tuple[int, int],
    g2: tuple[int, int],
    expanded_row: set[int],
    expanded_col: set[int],
    expansion_factor: int = 1,
):
    x1, y1 = g1
    x2, y2 = g2

    dist = abs(x2 - x1) + abs(y2 - y1)
    for x in range(min(x1, x2), max(x1, x2)):
        if x in expanded_row:
            dist += expansion_factor
    for y in range(min(y1, y2), max(y1, y2)):
        if y in expanded_col:
            dist += expansion_factor

    return dist


def sum_shortest_path(
    galaxies: list[tuple[int, int]],
    expanded_row: set[int],
    expanded_col: set[int],
    expansion_factor: int = 1,
) -> int:
    sum_dist = 0
    for i in range(len(galaxies)):  # pylint: disable=consider-using-enumerate
        for j in range(i + 1, len(galaxies)):
            g1, g2 = galaxies[i], galaxies[j]
            sum_dist += find_shortest_path(
                g1, g2, expanded_row, expanded_col, expansion_factor
            )

    return sum_dist


def find_galaxies_and_expanded_row_col(
    lines: list[str],
) -> tuple[list[tuple[int, int]], set[int], set[int]]:
    galaxies = []
    expanded_row = set(range(0, len(lines)))
    expanded_col = set(range(0, len(lines[0])))

    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == "#":
                galaxies.append((i, j))
                if i in expanded_row:
                    expanded_row.remove(i)
                if j in expanded_col:
                    expanded_col.remove(j)

    return galaxies, expanded_row, expanded_col


if __name__ == "__main__":
    with open("input.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        galaxies, expanded_row, expanded_col = find_galaxies_and_expanded_row_col(lines)
        print(len(galaxies))
        sum_dist = sum_shortest_path(galaxies, expanded_row, expanded_col)
        print(f"Sum of shortest path: {sum_dist}")

        # part 2
        sum_dist = sum_shortest_path(
            galaxies, expanded_row, expanded_col, expansion_factor=1_000_000 - 1
        )
        print(f"Sum of shortest path: {sum_dist}")
