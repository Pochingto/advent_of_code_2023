RED = 12
GREEN = 13
BLUE = 14

def is_possible(red: int, green: int, blue: int) -> bool:
    return red <= RED and green <= GREEN and blue <= BLUE

def parse_set(s: str) -> tuple[int, int, int]:
    cubes = s.split(",")
    counts = [0, 0, 0]
    for cube in cubes: 
        cube = cube.strip()
        count, color = cube.split(" ")
        if color == "red": 
            counts[0] = int(count)
        elif color == "green": 
            counts[1] = int(count)
        elif color == "blue": 
            counts[2] = int(count)
        else: 
            raise ValueError(f"Unknown color: {color}")

    return tuple(counts)

def is_possible_game(line: str) -> bool:
    line = line[line.find(":") + 2:]
    sets = line.split(";")

    for s in sets: 
        red, green, blue = parse_set(s)
        if not is_possible(red, green, blue):
            return False
    return True

def get_power_game(line: str) -> int: 
    line = line[line.find(":") + 2:]
    sets = line.split(";")
    at_least = [0, 0, 0]
    for s in sets: 
        red, green, blue = parse_set(s)
        if red > at_least[0]:
            at_least[0] = red
        if green > at_least[1]:
            at_least[1] = green
        if blue > at_least[2]:
            at_least[2] = blue
            
    power = at_least[0] * at_least[1] * at_least[2]
    return power

if __name__ == "__main__": 
    with open("input.txt", "r") as f: 
        lines = f.readlines()
        sum_id = 0
        for i, line in enumerate(lines): 
            if is_possible_game(line): 
                sum_id += (i + 1)

        print(f"sum_id: {sum_id}")

        powers = list(map(get_power_game, lines))
        sum_power = sum(powers)
        print(f"sum_power: {sum_power}")