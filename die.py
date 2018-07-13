from random import randint

class Die():
    """A class representing a single dice"""

    def __init__(self, num_sides=6):
        """Assume a 6-sides die"""
        self.num_sides = num_sides

    def roll(self):
        """Return a random value betwenn 1 and Num_sides"""
        return randint(1, self.num_sides)
