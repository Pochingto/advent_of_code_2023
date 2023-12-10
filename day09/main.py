def calculate_diffs(nums: list[int]) -> list[int]:
    diffs = [0] * (len(nums) - 1)
    for i in range(1, len(nums)):
        diffs[i - 1] = nums[i] - nums[i - 1]
    return diffs


def is_all_zeros(nums: list[int]) -> bool:
    for num in nums:
        if num != 0:
            return False
    return True


def extrapolate(nums: list[int]) -> int:
    seqs = []
    seqs.append(nums)
    last_seq = nums
    while not is_all_zeros(last_seq):
        last_seq = calculate_diffs(last_seq)
        seqs.append(last_seq)

    last = 0
    for i in range(len(seqs) - 1, -1, -1):
        last += seqs[i][-1]
    return last


def extrapolate_backward(nums: list[int]) -> int:
    seqs = []
    seqs.append(nums)
    last_seq = nums
    while not is_all_zeros(last_seq):
        last_seq = calculate_diffs(last_seq)
        seqs.append(last_seq)

    first = 0
    for i in range(len(seqs) - 1, -1, -1):
        first = seqs[i][0] - first
    return first


def parse_line(line: str) -> list[int]:
    return [int(num) for num in line.strip().split(" ")]


if __name__ == "__main__":
    with open("input.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

        s = 0
        for line in lines:
            nums = parse_line(line)
            # print(nums)
            # s += extrapolate(nums)
            s += extrapolate_backward(nums)

        print(f"total sum: {s}")
