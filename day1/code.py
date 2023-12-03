LETTER2DIGIT = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5', 
    'six': '6',
    'seven': '7', 
    'eight': '8',
    'nine': '9'
}
LETTERS = ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')

def read_input(line: str) -> int: 
    first = None
    last = None
    for c in line: 
        if c.isdigit(): 
            if first is None: 
                first = c
            last = c

    return int(first + last)

def find_first_last_digit(line: str) -> tuple[int, int]: 
    first = len(line) + 1
    last = -1
    for i, c in enumerate(line): 
        if c.isdigit(): 
            if first == len(line) + 1: 
                first = i
            last = i
    return first, last

def find_first_last_letter(line: str) -> tuple[str, int, str, int]:
    first_letter, first_idx = "", len(line) + 1
    last_letter, last_idx = "", -1

    for letter in LETTERS:
        idx = line.find(letter)
        if idx != -1 and idx < first_idx:
            first_idx = idx
            first_letter = letter

        idx = line.rfind(letter)
        if idx != -1 and idx > last_idx:
            last_idx = idx
            last_letter = letter

    return first_letter, first_idx, last_letter, last_idx

def read_line(line: str) -> int:
    try: 
        first_digit_idx, last_digit_idx = find_first_last_digit(line)
        first_letter, first_letter_idx, last_letter, last_letter_idx = find_first_last_letter(line)

        first = None
        last = None
        if first_digit_idx < first_letter_idx:
            first = line[first_digit_idx]
        else:
            first = LETTER2DIGIT[first_letter]
        
        if last_digit_idx > last_letter_idx:
            last = line[last_digit_idx]
        else:
            last = LETTER2DIGIT[last_letter]

        # print("=" * 10)
        # print(f"{line}: len {len(line)}")
        # print(first_digit_idx, first_letter_idx)
        # print(last_digit_idx, last_letter_idx)
        # print(first + last)
        return int(first + last)
    except Exception as e: 
        print(e)
        print(line)
        raise ValueError

def replace_first_letter(line: str) -> str: 
    letter_idx = []
    for letter in LETTERS:
        idx = line.find(letter)
        if idx != -1: 
            letter_idx.append((letter, idx))
    
    letter_idx = sorted(letter_idx, key=lambda x: x[1])
    if len(letter_idx) != 0: 
        first_letter, first_letter_idx = letter_idx[0]
        line = line[:first_letter_idx] + LETTER2DIGIT[first_letter] + line[first_letter_idx + len(first_letter):]
    
    return line

def replace_last_letter(line: str) -> str:
    letter_idx = []
    for letter in LETTERS:
        idx = line.rfind(letter)
        if idx != -1: 
            letter_idx.append((letter, idx))

    letter_idx = sorted(letter_idx, key=lambda x: x[1], reverse=True)
    if len(letter_idx) != 0: 
        last_letter, last_letter_idx = letter_idx[0]
        line = line[:last_letter_idx] + LETTER2DIGIT[last_letter] + line[last_letter_idx + len(last_letter):]

    return line

def replace_letters(line: str) -> str:
    line = replace_first_letter(line)
    line = replace_last_letter(line)
    return line

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = f.readlines()
        nums = list(map(read_line, lines))
        total_sum = sum(nums)
        print("Total sum: ", total_sum)

    with open("day_1_1_output.txt", "w") as f: 
        f.write("\n".join(list(map(str, nums))))