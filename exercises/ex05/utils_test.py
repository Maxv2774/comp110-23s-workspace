"""unit test for utils!"""
__author__ = "730605138"
from utils import only_evens, sub, concat


def test_only_evens() -> None:
    """Unit test for only_evens."""
    assert only_evens([1, 2, 3]) == [2]
    assert only_evens([1, 5, 3]) == []
    assert only_evens([4, 4, 4]) == [4, 4, 4]


def test_concat() -> None:
    """Unit test for concat."""
    assert concat([1, 2], [3, 4]) == [1, 2, 3, 4]
    assert concat(["dog", "cat"], ["frog"]) == ["dog", "cat", "frog"]
    assert concat([1, 2], []) == [1, 2]


def test_sub() -> None:
    """Unit test for sub."""
    assert sub([10, 20, 30, 40], 1, 3) == [20, 30]
    assert sub([0, 1, 2, 3, 4, 5], 3, 5) == [3, 4]
    assert sub([0, 1, 2, 3, 4, 5], 0, 5) == [0, 1, 2, 3, 4]
    assert sub([], 0, 5) == []
    assert sub([1, 2, 3, 4], -1, 4) == [1, 2, 3, 4]
    assert sub([1, 2, 3, 4], 0, 10) == [1, 2, 3, 4]
