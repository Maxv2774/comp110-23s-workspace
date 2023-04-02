"""Unit Test for sum function"""

from sum import sum

def test_empty() -> None:
    assert sum([]) == 0

def test_one_element() -> None:
    assert sum([1.0]) == 1

def test_many() -> None:
    assert sum([1.0, 2.0, 3.0]) == 6

def test_negatives() -> None:
    assert sum([1.0,-2.0,1.0]) == 0
