from Card import Card


class Deck(Card):
    def __init__(self, cards):
        Card.__init__(self)
        self.cards = cards

    def Deck_pop(self, i):
        self.cards.pop(i)

    def find_idx(self, x):
        return self.cards.index(x)

    def __str__(self):
        return str(self.cards)

    def __len__(self):
        return len(self.cards)
