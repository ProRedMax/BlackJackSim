import random

import Card


class Deck:
    cards: list

    def shuffle(self):
        random.shuffle(self.cards)

    def __str__(self):
        return_string = ""
        for card in self.cards:
            return_string = return_string + str(card) + "  "
        return return_string

    def __init__(self, count=1):
        extract = []
        self.cards = [Card.Card(11, True) * 4 * count, Card.Card(2, False) * 4 * count, Card.Card(3, False) * 4 * count,
                      Card.Card(4, False) * 4 * count,
                      Card.Card(5, False) * 4 * count, Card.Card(6, False) * 4 * count, Card.Card(7, False) * 4 * count,
                      Card.Card(8, False) * 4 * count,
                      Card.Card(9, False) * 4 * count, Card.Card(10, False) * 16 * count]
        for inner in self.cards:
            extract.extend(inner)
        self.cards = extract

    def pop(self):
        return self.cards.pop()
