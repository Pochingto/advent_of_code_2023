from collections import deque


def map_source_to_dest(src: int, src_dest_map: list[tuple[int, int, int]]) -> int:
    for dest_start, src_start, length in src_dest_map:
        if src in range(src_start, src_start + length):
            return dest_start + (src - src_start)

    return src


def parse_map_line(line: str) -> tuple[int, int, int]:
    # print("called parse map")
    return tuple(int(num.strip()) for num in line.strip().split(" ") if len(num) > 0)


def parse_map(lines: list[str]) -> list[tuple[int, int, int]]:
    maps = []
    for line in lines:
        if len(line) > 0:
            maps.append(parse_map_line(line))
    return maps


def get_next_map(lines: list[str], header: str) -> list(tuple[int, int, int]):
    start = 0
    while start < len(lines) and not lines[start].startswith(header):
        start += 1
    start += 1

    end = start + 1
    while end < len(lines) and len(lines[end]) > 3:
        end += 1

    # print(f"get next map: {header}")
    # print(lines[start: end])
    return parse_map(lines[start:end])


def parse_seed_range(line: str) -> list[tuple[int, int]]:
    seeds = line[line.find(":") + 1 :]
    seeds = [int(seed.strip()) for seed in seeds.strip().split(" ") if len(seed) > 0]

    seed_ranges = []
    for i in range(0, len(seeds), 2):
        seed_ranges.append((seeds[i], seeds[i] + seeds[i + 1]))
    return seed_ranges


def parse_seed(line: str) -> list[int]:
    seeds = line[line.find(":") + 1 :]
    seeds = [int(seed.strip()) for seed in seeds.strip().split(" ") if len(seed) > 0]
    return seeds


def calculate_lowest_location(lines: list[str]) -> int:
    seeds = parse_seed(lines[0])
    MAPS = [
        "seed-to-soil",
        "soil-to-fertilizer",
        "fertilizer-to-water",
        "water-to-light",
        "light-to-temperature",
        "temperature-to-humidity",
        "humidity-to-location",
        "dummy",
    ]

    lowest_location = float("inf")
    lines = lines[2:]
    for seed in seeds:
        # print(f"================== seed: {seed}==================")
        current = 0
        maps = []
        starting_map = False
        src = seed

        for line in lines:
            # print(f"line: {line}, len: {len(line)}")
            # print(f"{line} . startswith {MAPS[current]} : {line.startswith(MAPS[current])}")
            if len(line) <= 1:
                src = map_source_to_dest(src, maps)
                # print(f"maps: {maps}")
                # print(f"src changed to {src}")
                starting_map = False
                maps = []
                current += 1
            elif starting_map:
                maps.append(parse_map_line(line))
            elif line.startswith(MAPS[current]):
                # print(f"Current: {MAPS[current]}")
                starting_map = True

        # print(f"location: {src}")
        if src < lowest_location:
            lowest_location = src

    return lowest_location


def transform_interval(
    interval: tuple[int, int], mappings: list[tuple[int, int, int]]
) -> list[tuple[int, int]]:
    start, end = interval
    last_start, last_end = None, None
    # 90, 99
    transformed = []

    while start < end and (start != last_start or end != last_end):
        last_start, last_end = start, end
        for mapping in mappings:
            dest, src, length = mapping
            # 56, 93, 4
            offset = dest - src
            if start in range(src, src + length):
                if end - 1 in range(src, src + length):
                    transformed.append((start + offset, end + offset))
                    return transformed
                transformed.append(
                    (start + offset, src + length + offset)
                )  # 50, 52
                start = src + length
            elif end - 1 in range(src, src + length):
                transformed.append((src + offset, end + offset))
                end = src

        if start >= end:
            raise Exception(
                f"assumed impossible:\n intervals: {interval}\n mappings: {mappings}\n"
            )

    if start < end:
        transformed.append((start, end))
    return transformed


def calculate_lowest_location_range(lines: list[str]) -> int:
    seeds = parse_seed_range(lines[0])
    MAPS = [
        "seed-to-soil",
        "soil-to-fertilizer",
        "fertilizer-to-water",
        "water-to-light",
        "light-to-temperature",
        "temperature-to-humidity",
        "humidity-to-location",
    ]

    lines = lines[2:]

    seed_ranges = deque()
    for seed in seeds:
        # print(f"================== seed: {seed}==================")
        seed_ranges.append(seed)

    current = 0
    # print(f"Initial seed ranges: {seed_ranges}")
    while current < len(MAPS):
        maps = get_next_map(lines, MAPS[current])
        len_seed_ranges = len(seed_ranges)
        for _ in range(len_seed_ranges):
            seed_range = seed_ranges.popleft()
            new_ranges = transform_interval(seed_range, maps)

            for r in new_ranges:
                seed_ranges.append(r)

        # print(f"After {MAPS[current]}, current seed_ranges: {seed_ranges}")
        current += 1

    lowest_location = float("inf")
    for seed_range in seed_ranges:
        start, _ = seed_range
        lowest_location = min(lowest_location, start)

    return lowest_location


if __name__ == "__main__":
    with open("input.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        lowest_location = calculate_lowest_location(lines)
        print(f"lowest: {lowest_location}")

        # 640121624 too high

        lowest_range = calculate_lowest_location_range(lines)
        print(f"lowest range: {lowest_range}")

        # 23922490 too low
