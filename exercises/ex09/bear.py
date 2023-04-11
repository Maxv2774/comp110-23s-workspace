"""File to define Bear class."""
__author__ = "730605138"


class Bear:
    """Bear Class."""

    def __init__(self, age_in: int = 0, hunger_score_in: int = 0):
        """Init method bear!"""
        self.age = age_in
        self.hunger_score = hunger_score_in
        return None
    
    def eat(self, num_fish: int):
        """Eat method for bear!"""
        self.hunger_score += num_fish
        return None
    
    def one_day(self):
        """One_day method for bear!"""
        self.age += 1
        self.hunger_score -= 1
        return None
