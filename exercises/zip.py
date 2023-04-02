"""Challenge Question !"""
__author__ = "730605138"

def zip(l1: list[str], l2: list[int]):
    if len(l1) != len(l2):
        return {}
    out = {}
    for i,j in enumerate(l1):
        out[j] = l2[i]
    return out

