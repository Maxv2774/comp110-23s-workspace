"""File to define River class."""

__author__ = "730605138"

from fish import Fish
from bear import Bear


class River:
    """River class."""

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        self.num_fish = num_fish
        self.num_bears = num_bears
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def bears_eating(self):
        """Bears eating!"""
        for i in self.bears:
            if self.num_fish > 5:
                i.eat(3)
                self.remove_fish(3)
        return None
    
    def check_hunger(self):
        """Check hunger."""
        bears = []
        for i in self.bears:
            if i.hunger_score >= 0:
                bears.append(i)
        self.num_bears = len(bears)
        self.bears = bears
        return None
                
    def check_ages(self):
        """Check_ages."""
        fish = []
        bear = []
        for x in self.fish:
            if x.age < 4:
                fish.append(x)
        for y in self.bears:
            if y.age < 6:
                bear.append(y)
        self.num_fish = len(fish)
        self.num_bears = len(bear)
        self.fish = fish
        self.bear = bear
        return None
    
    def remove_fish(self, amount: int):
        """Remove fish."""
        self.fish = self.fish[amount:]
        self.num_fish = self.num_fish - amount
        return None
        
    def repopulate_fish(self):
        """Repopulate_fish yes."""
        x = ((self.num_fish // 2) * 4)
        self.num_fish =+ x
        for i in range(x):
            self.fish.append(Fish())
        return None
    
    def repopulate_bears(self):
        """Repopaulte bears."""
        x = (self.num_bears // 2)
        self.num_bears = self.num_bears + x
        for i in range(x):
            self.bears.append(Bear())
        return None
    
    def view_river(self):
        """See whats in the river."""
        print(f"~~~ Day {self.day}: ~~~ \nFish population: {self.num_fish}\nBear population: {self.num_bears}")
        return None
            
    def one_river_day(self):
        """One day Simulation."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()
        return None

    def one_river_week(self):
        """One day times 7."""
        for i in range(7):
            self.one_river_day()
        return None

            
