"""Example function for unit test"""

def sum(ls: list[float]) -> float:
    out = 0
    for i in range(len(ls)):
        out += ls[i]
    return out
