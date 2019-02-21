class Card:
    def __init__(self):
        self.cart = {
            "A": 11,
            "K": 10,
            "Q": 10,
            "J": 10,
            "10": 10,
            "9": 9,
            "8": 8,
            "7": 7,
            "6": 6,
            "5": 5,
            "4": 4,
            "3": 3,
            "2": 2
        }
        self.keys = self.cart.keys()
        self.suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
        self.all_card = []
        for i in self.keys:
            for j in self.suits:
                self.all_card.append((i, j))

    def __len__(self):
        return len(self.all_card)
