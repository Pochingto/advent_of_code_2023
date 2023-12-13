def dfs(
    record: str,
    target: list[int],
    target_idx: int,
    current_construct: int,
    idx: int,
    cache: dict[tuple[int, int, int], int],
) -> int:
    if (target_idx, current_construct, idx) in cache:
        return cache[(target_idx, current_construct, idx)]

    if idx >= len(record):
        if current_construct == 0:
            return 1 if target_idx == len(target) else 0
        elif target_idx != len(target) - 1:
            return 0
        else:
            return 1 if current_construct == target[target_idx] else 0

    if record[idx] == ".":
        if current_construct == 0:
            cache[(target_idx, current_construct, idx)] = dfs(
                record, target, target_idx, 0, idx + 1, cache
            )
            return cache[(target_idx, current_construct, idx)]
        if target_idx >= len(target) or current_construct != target[target_idx]:
            return 0

        cache[(target_idx, current_construct, idx)] = dfs(
            record, target, target_idx + 1, 0, idx + 1, cache
        )
        return cache[(target_idx, current_construct, idx)]

    if record[idx] == "#":
        cache[(target_idx, current_construct, idx)] = dfs(
            record, target, target_idx, current_construct + 1, idx + 1, cache
        )
        return cache[(target_idx, current_construct, idx)]

    if record[idx] == "?":
        count = 0

        # choose "#"
        count += dfs(record, target, target_idx, current_construct + 1, idx + 1, cache)

        # choose "."
        if current_construct == 0:
            count += dfs(record, target, target_idx, 0, idx + 1, cache)
        elif target_idx >= len(target) or current_construct != target[target_idx]:
            count += 0
        else:
            count += dfs(record, target, target_idx + 1, 0, idx + 1, cache)

        cache[(target_idx, current_construct, idx)] = count
        return count


def parse_line(line: str) -> tuple[str, list[int]]:
    record, targets = line.split(" ")
    targets = [int(num) for num in targets.strip().split(",")]
    return record, targets


if __name__ == "__main__":
    with open("input.txt", "r", encoding="utf-8") as f:
        count = 0
        for line in f:
            record, targets = parse_line(line)
            cache = {}
            record = "?".join([record] * 5)
            targets *= 5
            # print(record)
            # print(targets)
            # break
            count += dfs(record, targets, 0, 0, 0, cache)

        print(f"count: {count}")
