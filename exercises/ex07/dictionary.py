"""Dictionjary utils!"""
__author__ = "730605138"


def invert(dic: dict[str, str]) -> dict[str, str]:
    """Takes a dictionary and switches the keys and the values."""
    values = list(dic.values())
    key = list(dic.keys())
    out = {}
    if len(set(values)) != len(values):
        raise KeyError
    else:
        for i in range(len(key)):
            out[values[i]] = key[i]
    return out


def favorite_color(dic: dict[str, str]) -> str:
    """Takes a dictionary and returns most occuring value."""
    out = {}
    for i in set(dic.values()):
        out[i] = list(dic.values()).count(i)
    largest = list(out.keys())[0]
    for key, value in out.items():
        if value >= out[largest]:
            largest = key
    return largest
  
  
def count(l1: list[str]) -> dict[str, int]:
    """Takes a list and creates a dictionary where the values are the count of the list."""
    out = {}
    for i in set(l1):
        out[i] = l1.count(i) 
    return out
