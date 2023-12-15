from main import *

def test_part1_hash():
    assert hash("rn=1") == 30
    assert hash("cm-") == 253
    assert hash("qp=3") == 97
    assert hash("cm=2") == 47
    assert hash("qp-") == 14
    assert hash("pc=4") == 180
    assert hash("ot=9") == 9
    assert hash("ab=5") == 197
    assert hash("pc-") == 48
    assert hash("pc=6") == 214
    assert hash("ot=7") == 231
    
def test_part2_hash_map(): 
    strings = [
        "rn=1", 
        "cm-", 
        "qp=3", 
        "cm=2", 
        "qp-", 
        "pc=4", 
        "ot=9",
        "ab=5", 
        "pc-", 
        "pc=6", 
        "ot=7"
    ]

    boxes = part2_hash_map(strings)
    assert boxes[0] == [("rn", 1), ("cm", 2)]
    assert boxes[3] == [("ot", 7), ("ab", 5), ("pc", 6)]
    for i, box in enumerate(boxes): 
        if i != 0 and i != 3: 
            assert len(box) == 0

def test_calculate_focal_power(): 
    boxes = [[] for _ in range(256)]
    boxes[0] = [("rn", 1), ("cm", 2)]
    boxes[3] = [("ot", 7), ("ab", 5), ("pc", 6)]

    assert calculate_focal_power(boxes) == 145