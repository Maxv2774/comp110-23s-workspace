"""Unit test for dictionary problems."""

from exercises.ex07.dictionary import invert, count, favorite_color


def test_invert1() -> None:
    """Base Case 1."""
    assert invert({"one": "1", "two": "2"}) == {"1": "one", "2": "two"}


def test_invert2() -> None:
    """Base Case 2."""
    assert invert({"1": "one", "2": "two"}) == {"one": "1", "two": "2"}


def test_invert() -> None:
    """Edge Case 1."""
    assert invert({}) == {}


def test_count1() -> None:
    """Base Case 1."""
    assert count(["help", "help", "help", "yes", "yes"]) == {"help": 3, "yes": 2}


def test_count2() -> None:
    """Base Case 2."""
    assert count(["help", "help", "yes", "yes"]) == {"help": 2, "yes": 2}


def test_count3() -> None:
    """Edge Case 1."""
    assert count([]) == {}


def test_favorite_color1() -> None:
    """Base Case 1."""
    assert favorite_color({"max": "blue", "hank": "green", "brick": "blue"}) == "blue"


def test_favorite_color2() -> None:
    """Base Case 2."""
    assert favorite_color({"max": "blue", "hank": "green", "brick": "green"}) == "green"


def test_favorite_color3() -> None:
    """Edge Case 1."""
    assert favorite_color({"max": "green", "hank": "green", "brick": "blue"}) == "green"
