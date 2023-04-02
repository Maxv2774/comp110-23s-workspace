"""Utils and unit test!"""
__author__ = "730605138"


def only_evens(l1: list[int]) -> list[int]:
    """Takes in a list of ints and returns all the evens."""
    out = []
    for i in l1:
        if i % 2 == 0: 
            out.append(i)
    return out


def concat(l1: list[int], l2: list[int]) -> list[int]:
    """Takes in two list and returns 1 list with list 2 at the end."""
    out = []
    for i in l1:
        out.append(i)
    for i in l2:
        out.append(i)
    return out


def sub(l1: list[int], a: int, b: int) -> list[int]:
    """Slices the list on the given indexes."""
    if len(l1) == 0 or len(l1) < a:
        return []
    if a < 0:
        a = 0
    if b > len(l1):
        b = len(l1)
    out = []
    for i in range(a, b):
        out.append(l1[i])
    return out
