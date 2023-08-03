import dataclasses

@dataclasses.dataclass
class Card:
    value: int
    isAce: bool

    def __init__(self, value, ace):
        """
        Initialize a card
        :param value:
        :param ace:
        """
        self.value = value
        self.isAce = ace


    def __mul__(self, other: int):
        return [Card(self.value, self.isAce) for _ in range(other)]

    def __str__(self):
        if self.isAce:
            return "Ace (1/11)"
        else:
            return str(self.value)