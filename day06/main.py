def ways_to_win(time: int, dist: int) -> int:
    ways = 0
    for t in range(time):
        dist_travel = (time - t) * t
        if dist_travel > dist:
            ways += 1
    return ways


def product_ways_to_win(times: list[int], dists: list[int]) -> int:
    product = 1
    for time, dist in zip(times, dists):
        product *= ways_to_win(time, dist)
    return product


def parse_lines(lines: list[str]) -> tuple[list[int], list[int]]:
    times = lines[0][lines[0].find(":") + 1 :]
    times = [int(time.strip()) for time in times.strip().split(" ") if len(time) > 0]

    dists = lines[1][lines[1].find(":") + 1 :]
    dists = [int(dist.strip()) for dist in dists.strip().split(" ") if len(dist) > 0]

    return times, dists


def parse_part2_lines(lines: list[str]) -> tuple[list[int], list[int]]:
    time = lines[0][lines[0].find(":") + 1 :]
    dist = lines[1][lines[1].find(":") + 1 :]
    return int(time.strip().replace(" ", "")), int(dist.strip().replace(" ", ""))


if __name__ == "__main__":
    with open("input.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        print(lines)
        times, dists = parse_lines(lines)
        print(times, dists)
        product = product_ways_to_win(times, dists)

        print(f"product: {product}")

        time, dist = parse_part2_lines(lines)
        print(time, dist)
        way = ways_to_win(time, dist)

        print(f"ways: {way}")
