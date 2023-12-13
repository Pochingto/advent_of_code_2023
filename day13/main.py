from typing import Callable


def is_vertically_reflected(lines: list[str], i: int) -> bool:
    l, r = i, i + 1
    while l >= 0 and r < len(lines[0]):
        for line in lines:
            ll, lr = line[l], line[r]
            if ll != lr:
                return False
        l -= 1
        r += 1

    return True


def is_vertically_reflected_smudged(lines: list[str], i: int) -> bool:
    l, r = i, i + 1
    smudged = False
    while l >= 0 and r < len(lines[0]):
        for line in lines:
            ll, lr = line[l], line[r]
            if ll != lr and smudged:
                return False
            elif ll != lr and not smudged:
                smudged = True
        l -= 1
        r += 1

    return True and smudged


def is_horizontally_reflected(lines: list[str], i: int) -> bool:
    l, r = i, i + 1
    while l >= 0 and r < len(lines):
        if lines[l] != lines[r]:
            return False
        l -= 1
        r += 1

    return True


def is_horizontally_reflected_smudged(lines: list[str], i: int) -> bool:
    l, r = i, i + 1
    smudged = False
    while l >= 0 and r < len(lines):
        for ll, lr in zip(lines[l], lines[r]):
            if ll != lr and smudged:
                return False
            elif ll != lr and not smudged:
                smudged = True
        l -= 1
        r += 1

    return True and smudged


def find_pattern_reflection(
    lines: list[str],
    possible_ranges: int,
    is_reflected: Callable[[list[str], int], bool],
) -> int:
    possible_reflections = set(range(possible_ranges))
    for i in range(possible_ranges):
        if i in possible_reflections and not is_reflected(lines, i):
            possible_reflections.remove(i)

    try:
        assert len(possible_reflections) <= 1
    except AssertionError as e:
        print("Found multiple reflection.")
        print(f"Possible reflections: {possible_reflections}")
        print("Pattern: ")
        for line in lines:
            print(line)
        raise e

    return possible_reflections.pop() + 1 if len(possible_reflections) == 1 else -1


def parse_pattern(lines: list[str]) -> list[list[str]]:
    patterns = []
    current_patterns = []
    for line in lines:
        if len(line) <= 1:
            patterns.append(current_patterns)
            current_patterns = []
        else:
            current_patterns.append(line.strip())

    if len(current_patterns) != 0:
        patterns.append(current_patterns)
    return patterns


def print_patterns(patterns: list[str]):
    for p in patterns:
        for l in p:
            print(l)

        print("=" * 20)


if __name__ == "__main__":
    with open("input.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        patterns = parse_pattern(lines)
        # print_patterns(patterns)

        summary = 0
        for pattern in patterns:
            vertical_reflection = find_pattern_reflection(
                pattern, len(pattern[0]) - 1, is_vertically_reflected
            )
            horizontal_reflection = find_pattern_reflection(
                pattern, len(pattern) - 1, is_horizontally_reflected
            )

            assert (
                vertical_reflection == -1 or horizontal_reflection == -1
            ), "Only one type of reflection"
            if vertical_reflection != -1:
                summary += vertical_reflection
            if horizontal_reflection != -1:
                summary += horizontal_reflection * 100

            # print(vertical_reflection)
            # print(horizontal_reflection)

        print(f"Part 1 Total summary: {summary}")

        # part 2
        summary = 0
        for pattern in patterns:
            vertical_reflection = find_pattern_reflection(
                pattern, len(pattern[0]) - 1, is_vertically_reflected_smudged
            )
            horizontal_reflection = find_pattern_reflection(
                pattern, len(pattern) - 1, is_horizontally_reflected_smudged
            )

            assert (
                vertical_reflection == -1 or horizontal_reflection == -1
            ), "Only one type of reflection"
            if vertical_reflection != -1:
                summary += vertical_reflection
            if horizontal_reflection != -1:
                summary += horizontal_reflection * 100

            # print(vertical_reflection)
            # print(horizontal_reflection)

        print(f"Part 2 Total summary: {summary}")
