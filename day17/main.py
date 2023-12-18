from queue import PriorityQueue


def get_left_right_dirs(direction: str) -> tuple[str, str]:
    if direction == ">" or direction == "<":
        return "^", "v"
    if direction == "^" or direction == "v":
        return "<", ">"
    raise ValueError("unknown direction")


def get_next_i_j(i: int, j: int, direction: str) -> tuple[int, int]:
    if direction == ">":
        return i, j + 1
    if direction == "<":
        return i, j - 1
    if direction == "^":
        return i - 1, j
    if direction == "v":
        return i + 1, j
    raise ValueError("unknown direction")


def dijkstra_algo(graph: list[str]) -> int:
    pq = PriorityQueue()
    pq.put((0, 0, 0, ">", 0))

    visited = set()
    while pq:
        dist, i, j, direction, count = pq.get()
        # visited.add((i, j))
        if i == len(graph) - 1 and j == len(graph[i]) - 1:
            return dist

        for neighbor_dir in get_left_right_dirs(direction):
            next_i, next_j = get_next_i_j(i, j, neighbor_dir)
            if next_i < 0 or next_i >= len(graph):
                continue
            if next_j < 0 or next_j >= len(graph[i]):
                continue

            if not (next_i, next_j, neighbor_dir, 1) in visited:
                visited.add((next_i, next_j, neighbor_dir, 1))
                pq.put(
                    (dist + int(graph[next_i][next_j]), next_i, next_j, neighbor_dir, 1)
                )

        if count < 3:
            next_i, next_j = get_next_i_j(i, j, direction)
            if next_i < 0 or next_i >= len(graph):
                continue
            if next_j < 0 or next_j >= len(graph[i]):
                continue
            if not (next_i, next_j) in visited:
                visited.add((next_i, next_j, direction, count + 1))
            pq.put(
                (
                    dist + int(graph[next_i][next_j]),
                    next_i,
                    next_j,
                    direction,
                    count + 1,
                )
            )

    raise Exception("cannot reach bottom right")


if __name__ == "__main__":
    with open("input.txt", "r", encoding="utf-8") as f:
        graph = [line.strip() for line in f]
        dist = dijkstra_algo(graph)
        print(f"Least heat loss: {dist}")
