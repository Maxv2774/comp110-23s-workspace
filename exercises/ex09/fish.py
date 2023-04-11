"""File to define Fish class."""
_author__ = "730605138"


class Fish:
    """Fish Class."""

    def __init__(self, age_in: int = 0):
        """Init method for fish!"""
        self.age = age_in
        return None
    
    def one_day(self):
        """One_day method for fish!"""
        self.age += 1
        return None