from Card import Card


class Hand:
    def __init__(self):
        self.Card_in_hand = []
        self.value = 0
        self.aces = 0

    def add_card(self, cart, value):
        self.Card_in_hand.append(cart)
        if value == 11:
            self.aces = self.aces + 1
        self.value = self.value + value

        if self.value > 21 and self.aces >= 1:
            self.value = self.value - 10  # if i have 21+ and i have 1 ace , ace now == 1 and not 11
            self.aces = self.aces - 1  # -1 ace its no more ace now i have 1 and not 11

    def hand_win(self):
        if (self.value) == 21:
            return "Win"
        elif (self.value) > 21:
            return "Lose"
        else:
            return "Go on"

    def __str__(self):
        return "{" + str(self.Card_in_hand) + "," + str(self.value) + "}"


class Beautiful_printing:
    @staticmethod
    def Hand_printing(player):
        x = str(player)
        x = x.replace(" ", "")
        x = x[3:len(x) - 5]
        x = x.replace("[", "")
        x = x.replace("]", "")
        x = x.replace(")", "")
        x = x.replace("(", "")
        x = x.replace("'", "")
        x = x.split(',')
        y = 0
        for _ in range(len(x)):
            if (y + 1) < len(x):
                print(" ---------------------")
                print("  | {} {}     |".format(x[y], x[y + 1]))
                print(" ---------------------")
                y = y + 2
        print(player.value)  # For people who do not understand in Card

    @staticmethod
    def dealer_printing(dealer):
        x = str(dealer)
        x = x.replace(" ", "")
        x = x[3:len(x) - 5]
        x = x.replace("[", "")
        x = x.replace("]", "")
        x = x.replace(")", "")
        x = x.replace("(", "")
        x = x.replace("'", "")
        x = x.split(',')
        print("~ Dealer Hand  ~")
        print("~~~~~~~~~~~~~~~~")
        if x[0] == '':
            print("No cart")

        elif len(x) == 2:
            print(" ------------------")
            print("  | {} {}     |".format(x[0], x[1]))
            print(" ------------------")

        else:
            print(" ---------------------     -------------------")
            print("  | {} {}        |     |#################|".format(
                x[0], x[1]))
            print(" ---------------------     -------------------")
        print(" ")