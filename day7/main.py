import functools

HANDS_ORDER = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]


def determine_hands_type(hand: str) -> int:
    counts = {}
    for s in hand:
        counts[s] = counts.get(s, 0) + 1

    if len(counts.keys()) == 1:
        return 7
    if len(counts.keys()) == 2:
        for k, v in counts.items():
            if v == 4:
                return 6
        return 5
    if len(counts.keys()) == 3:
        for k, v in counts.items():
            if v == 3:
                return 4
        return 3
    if len(counts.keys()) == 4:
        return 2
    if len(counts.keys()) == 5:
        return 1

    raise Exception(f"unknown hands type... {hand}")


def compare_hands_order(hand1: str, hand2: str) -> int:
    assert len(hand1) == len(hand2), "hands length not equal"
    for h1, h2 in zip(hand1, hand2):
        if h1 != h2:
            if HANDS_ORDER.index(h1) > HANDS_ORDER.index(h2):
                return -1
            return 1

    raise Exception("equal hand... unhandled")


def compare_hands(hand1: str, hand2: str) -> int:
    type1, type2 = determine_hands_type(hand1), determine_hands_type(hand2)
    if type1 < type2:
        return -1
    if type1 > type2:
        return 1
    return compare_hands_order(hand1, hand2)


def parse_hands_bid(lines: list[str]) -> list[tuple[int, int]]:
    def parse_line(line: str) -> tuple[str, int]:
        hand, bid = line.split(" ")
        return hand, int(bid)

    return list(map(parse_line, lines))


def calculate_wins_sorted(hand_bids: list[tuple[int, int]]) -> int:
    wins = 0
    for i, (_, bid) in enumerate(hand_bids):
        wins += (i + 1) * bid
    return wins


def compare(hand_bid1, hand_bid2):
    h1, _ = hand_bid1
    h2, _ = hand_bid2
    return compare_hands(h1, h2)


if __name__ == "__main__":
    with open("input.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        hand_bids = parse_hands_bid(lines)
        print(hand_bids)
        print(f"sorted: ")
        hand_bids = sorted(hand_bids, key=functools.cmp_to_key(compare))
        print(f"{hand_bids}")

        print(f"wins: {calculate_wins_sorted(hand_bids)}")
