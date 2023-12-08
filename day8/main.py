import math


def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


def lcm_of_list(numbers):
    if not numbers:
        return 0
    current_lcm = numbers[0]
    for number in numbers[1:]:
        current_lcm = lcm(current_lcm, number)
    return current_lcm


def calculate_steps(
    start_node: str, instructions: str, lr_map: dict[str, tuple[str, str]]
) -> int:
    step = 0
    current = start_node

    max_iter = 1e10
    while True and step < max_iter:
        for instruction in instructions:
            dests = lr_map[current]
            if instruction == "L":
                current = dests[0]
            elif instruction == "R":
                current = dests[1]
            else:
                raise ValueError("instruction != L or R")

            step += 1
            if current == "ZZZ":
                return step
    raise ValueError("Max. iteration reached.")


def parse_input(line: str) -> str:
    return line.strip()


def parse_maps(lines: str) -> dict[str, tuple[str, str]]:
    lr_map = {}
    for line in lines:
        key = line[:3]
        open_paren = line.find("(")
        close_paren = line.find(")")
        left = line[open_paren + 1 : open_paren + 4]
        right = line[close_paren - 3 : close_paren]
        lr_map[key] = (left, right)

    return lr_map


def parse_start_nodes(lines: str) -> list[str]:
    start_nodes = []
    for line in lines:
        if line[2] == "A":
            start_nodes.append(line[:3])
    return start_nodes


def calculate_steps_part2(
    start_node: str, instructions: str, lr_map: dict[str, tuple[str, str]]
) -> tuple[int, int]:
    step = 0
    current = start_node
    first_Z, first_loop = None, None

    max_iter = 1e10
    visited = set()

    while True and step < max_iter:
        for i, instruction in enumerate(instructions):
            if (current, i) in visited and first_loop is None:
                first_loop = step
                print(f"Loop: {current}, start at {i}")
            visited.add((current, i))

            dests = lr_map[current]
            if instruction == "L":
                current = dests[0]
            elif instruction == "R":
                current = dests[1]
            else:
                raise ValueError("instruction != L or R")

            step += 1
            if current[-1] == "Z" and first_Z is None:
                first_Z = step
            if first_Z is not None and first_loop is not None:
                return first_Z, first_loop

    raise ValueError("Max. iteration reached.")


if __name__ == "__main__":
    with open("input.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        # print(lines)
        instructions = parse_input(lines[0])
        lr_map = parse_maps(lines[2:])

        # step = calculate_steps("AAA", instructions, lr_map)
        # print(f"total step: {step}")

        steps = []
        start_nodes = parse_start_nodes(lines[2:])
        print(start_nodes)
        for node in start_nodes:
            steps.append(calculate_steps_part2(node, instructions, lr_map))
            print(steps)
        print(steps)

        steps = [step[0] for step in steps]
        print(f"LCM: {lcm_of_list(steps)}")
