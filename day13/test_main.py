import pytest

from main import *


@pytest.fixture
def lines():
    with open("example.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        return lines


@pytest.fixture
def patterns(lines):
    return parse_pattern(lines)


def test_parse_pattern_len(lines):
    patterns = parse_pattern(lines)
    assert len(patterns) == 2


def test_horizontal_reflection(patterns):
    expected_output = [-1, 4]
    for pattern, output in zip(patterns, expected_output):
        reflection = find_pattern_reflection(
            pattern, len(pattern) - 1, is_horizontally_reflected
        )
        assert reflection == output


def test_vertical_reflection(patterns):
    expected_output = [5, -1]
    for pattern, output in zip(patterns, expected_output):
        reflection = find_pattern_reflection(
            pattern, len(pattern) - 1, is_vertically_reflected
        )
        assert reflection == output


def test_horizontal_smudged_reflection(patterns):
    expected_output = [3, 1]
    for pattern, output in zip(patterns, expected_output):
        reflection = find_pattern_reflection(
            pattern, len(pattern) - 1, is_horizontally_reflected_smudged
        )
        assert reflection == output


def test_vertical_smudged_reflection(patterns):
    expected_output = [-1, -1]
    for pattern, output in zip(patterns, expected_output):
        reflection = find_pattern_reflection(
            pattern, len(pattern) - 1, is_vertically_reflected_smudged
        )
        assert reflection == output
