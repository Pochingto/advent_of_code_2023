def map_source_to_dest(src: int, src_dest_map: list[tuple[int, int, int]]) -> int:
    for dest_start, src_start, length in src_dest_map:
        if src in range(src_start, src_start + length):
            return dest_start + (src - src_start)

    return src


def parse_map(line: list[str]) -> tuple[int, int, int]:
    # print("called parse map")
    return tuple(int(num.strip()) for num in line.strip().split(" ") if len(num) > 0)


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
                maps.append(parse_map(line))
            elif line.startswith(MAPS[current]):
                # print(f"Current: {MAPS[current]}")
                starting_map = True

        # print(f"location: {src}")
        if src < lowest_location:
            lowest_location = src

    return lowest_location


if __name__ == "__main__":
    with open("input.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        lowest_location = calculate_lowest_location(lines)
        print(f"lowest: {lowest_location}")

        # 640121624 too high
