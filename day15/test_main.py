from main import *

def test_hash():
    assert hash("HASH") == 52
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
    