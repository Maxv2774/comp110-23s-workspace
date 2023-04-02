"""ex04 utils !"""
__author__ = "730606138"


def all(l1: list[int], int1: int) -> bool:
    """Arguments: A list of integers and an int. Returns: A bool, True if all numbers match the indicated number, False otherwise or if the list is empty. This algorithm should work for a list of any length."""
    if len(l1) == 0:
        return False
    counter = 0
    while len(l1) > counter:
        if l1[counter] != int1:
            return False
        counter += 1
    return True


def max(l1: list[int]) -> int:
    """Argument: A list of integers.Returns: An int, the largest number in the list. If the list is empty, raises a ValueError."""
    if len(l1) == 0:
        raise ValueError("max() arg is an empty List")
    counter = 0
    out = l1[counter]
    while len(l1) > counter:
        if out < l1[counter]:
            out = l1[counter]
        counter += 1
    return out


def is_equal(l1: list[int], l2: list[int]) -> bool:
    """Parameters: Two lists of integers. Returns: True if lists are equal, False otherwise."""
    if len(l1) != len(l2):
        return False
    counter = 0
    while len(l1) > counter:
        if l1[counter] != l2[counter]:
            return False
        counter += 1
    return True
