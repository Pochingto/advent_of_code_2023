import sys


def get_reflection(dir: str, mirror: str) -> str:
    if mirror == "\\":
        if dir == "l":
            return "u"
        if dir == "r":
            return "d"
        if dir == "u":
            return "l"
        if dir == "d":
            return "r"
    if mirror == "/":
        if dir == "l":
            return "d"
        if dir == "d":
            return "l"
        if dir == "r":
            return "u"
        if dir == "u":
            return "r"
    return None


def get_next_move(i: int, j: int, dir: str) -> tuple[int, int]:
    if dir == "r":
        return i, j + 1
    if dir == "l":
        return i, j - 1
    if dir == "u":
        return i - 1, j
    if dir == "d":
        return i + 1, j
    raise ValueError("Unknown direction")


def travel_graph(
    graph: list[str], i: int, j: int, explored: set[tuple[int, int, str]], dir: str
) -> None:
    if i < 0 or i >= len(graph):
        return
    if j < 0 or j >= len(graph[i]):
        return

    if (i, j, dir) in explored:
        return
    explored.add((i, j, dir))
    # print(len(explored))

    if graph[i][j] == ".":
        next_i, next_j = get_next_move(i, j, dir)
        travel_graph(graph, next_i, next_j, explored, dir)
    elif graph[i][j] == "\\" or graph[i][j] == "/":
        dir = get_reflection(dir, graph[i][j])
        next_i, next_j = get_next_move(i, j, dir)
        travel_graph(graph, next_i, next_j, explored, dir)
    elif graph[i][j] == "-":
        if dir == "u" or dir == "d":
            next_i, next_j = get_next_move(i, j, "l")
            travel_graph(graph, next_i, next_j, explored, "l")
            next_i, next_j = get_next_move(i, j, "r")
            travel_graph(graph, next_i, next_j, explored, "r")
        elif dir == "l" or dir == "r":
            next_i, next_j = get_next_move(i, j, dir)
            travel_graph(graph, next_i, next_j, explored, dir)
    elif graph[i][j] == "|":
        if dir == "l" or dir == "r":
            next_i, next_j = get_next_move(i, j, "u")
            travel_graph(graph, next_i, next_j, explored, "u")
            next_i, next_j = get_next_move(i, j, "d")
            travel_graph(graph, next_i, next_j, explored, "d")
        elif dir == "u" or dir == "d":
            next_i, next_j = get_next_move(i, j, dir)
            travel_graph(graph, next_i, next_j, explored, dir)
    return


def get_energized(graph: list[str], i_start: int, j_start: int, dir_start: str) -> int:
    explored = set()

    travel_graph(graph, i_start, j_start, explored, dir_start)
    traveled = set()
    for i, j, _ in explored:
        traveled.add((i, j))
    return len(traveled)


if __name__ == "__main__":
    with open("input.txt", "r", encoding="utf-8") as f:
        graph = [line.strip() for line in f]
        # print(graph)
        sys.setrecursionlimit(len(graph) * len(graph[0]) * 4 * 2)

        max_energized = 0
        for i in range(len(graph)):
            energized = get_energized(graph, i, 0, "r")
            max_energized = max(energized, max_energized)
            energized = get_energized(graph, i, len(graph[i]) - 1, "l")
            max_energized = max(energized, max_energized)

        for j in range(len(graph[0])):
            energized = get_energized(graph, 0, j, "d")
            max_energized = max(energized, max_energized)
            energized = get_energized(graph, len(graph) - 1, j, "u")
            max_energized = max(energized, max_energized)
        print(f"max energized: {max_energized}")

        # graph_clone = [list(line) for line in graph]
        # for i in range(len(graph_clone)):
        #     for j in range(len(graph_clone[i])):
        #         if (i, j) in traveled:
        #             graph_clone[i][j] = "#"
        #         else:
        #             graph_clone[i][j] = "."

        #     print("".join(graph_clone[i]))
