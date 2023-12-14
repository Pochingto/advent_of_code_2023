import pytest

from main import *


@pytest.fixture
def example_north():
    with open("example_north.txt") as f:
        lines = [list(line.strip()) for line in f]
    return lines


@pytest.fixture
def example_before():
    with open("example_before.txt") as f:
        lines = [list(line.strip()) for line in f]
    return lines


@pytest.fixture
def example_1_circle():
    with open("example_1_circle.txt") as f:
        lines = [list(line.strip()) for line in f]
    return lines


@pytest.fixture
def example_2_circle():
    with open("example_2_circle.txt") as f:
        lines = [list(line.strip()) for line in f]
    return lines


@pytest.fixture
def example_3_circle():
    with open("example_3_circle.txt") as f:
        lines = [list(line.strip()) for line in f]
    return lines


def test_score_pattern(example_north):
    assert score_pattern(example_north) == 136

def test_score_part1(example_before):
    move_north(example_before)
    assert score_pattern(example_before) == 136


def test_move_north(example_before, example_north):
    north = example_north

    move_north(example_before)
    print(north)
    print(example_before)
    assert north == example_before


def test_circle(example_before, example_1_circle, example_2_circle, example_3_circle):
    move_circle(example_before)
    assert example_1_circle == example_before
    move_circle(example_before)
    assert example_2_circle == example_before
    move_circle(example_before)
    assert example_3_circle == example_before


def test_billions_cycle(example_before):
    move_multi_cycle(example_before, 1_000_000_000)
    pattern = ["".join(line) for line in example_before]
    assert score_pattern(pattern) == 64
