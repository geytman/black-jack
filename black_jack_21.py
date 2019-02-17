'''
    Welcome to BlackJack! Get as close to 21 as you can without going over! 
    Dealer hits until she reaches 17 . Aces count as 1 or 11
    At first player have 100 Chips , Game Over if player have 0 Chips Or When player Decides to leave


    *Python3.X Black_Jack_21

'''

import random


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
        print(player.value)  # For people who do not understand

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


class Error:
    @staticmethod
    def is_Error():
        while True:
            x = input()
            if x != "yes" and x != "no":
                print("Need be yes or no ")
            else:
                return x

    @staticmethod
    def Error_bet(have_Chip):
        while True:
            try:
                x = int(input())
            except:
                print("need to be int ")
            else:
                if x > have_Chip:
                    print("Sorry, You do not have enough Chips , you have {} ".
                          format(have_Chip))
                else:
                    return x
            finally:
                print("")


class Chips:  #  player Chips
    def __init__(self):
        self.total = 100

    def win_bet(self, num):
        self.total = self.total + num

    def lose_bet(self, num):
        self.total = self.total - num


# GAMEPLAY!
if __name__ == "__main__":

    player_Chips = Chips()
    print("Welcome to BlackJack!")

    while (True):
        print("How many chips would you like to bet? you have now {} ".format(
            player_Chips.total))
        y = Error().Error_bet(
            player_Chips.
            total)  # if y is int  , and you have Enough Chips to Play
        player = Hand()
        dealer = Hand()
        card_in_game = Deck(Card().all_card)

        #  1 card to dealer
        random_choice = random.choices(
            card_in_game.cards)  # random ...[('3', 'Hearts')]....
        card_in_game.Deck_pop(card_in_game.find_idx(
            random_choice[0]))  # pop obj in card_in_game by idx
        dealer.add_card(
            random_choice,
            card_in_game.cart[random_choice[0][0]])  # add card to player
        #  2 card to dealer
        random_choice = random.choices(
            card_in_game.cards)  # random ...[('3', 'Hearts')]....
        card_in_game.Deck_pop(card_in_game.find_idx(
            random_choice[0]))  # pop obj in card_in_game by idx
        dealer.add_card(
            random_choice,
            card_in_game.cart[random_choice[0][0]])  # add card to player
        Beautiful_printing().dealer_printing(
            dealer)  # print 2 card in player hand

        #  1 card to player
        random_choice = random.choices(
            card_in_game.cards)  # random ...[('3', 'Hearts')]....
        card_in_game.Deck_pop(card_in_game.find_idx(
            random_choice[0]))  # pop obj in card_in_game by idx
        player.add_card(
            random_choice,
            card_in_game.cart[random_choice[0][0]])  # add card to player
        #  2 card to player
        random_choice = random.choices(
            card_in_game.cards)  # random ...[('3', 'Hearts')]....
        card_in_game.Deck_pop(card_in_game.find_idx(
            random_choice[0]))  # pop obj in card_in_game by idx
        player.add_card(
            random_choice,
            card_in_game.cart[random_choice[0][0]])  # add card to player
        print("~ Player Hand  ~")
        print("~~~~~~~~~~~~~~~~")
        Beautiful_printing().Hand_printing(
            player)  # print 2 card in player hand

        for_loop_2 = player.hand_win()  # win , lose or go on
        while (True
               ):  # player win or not , if not player can take another card
            if (player.hand_win() == "Win"):
                print("player Win")
                for_loop_2 = player.hand_win()
                player_Chips.win_bet(y)
                break

            elif (player.hand_win() == "Lose"):
                print("player Lose")
                for_loop_2 = player.hand_win()
                player_Chips.lose_bet(y)
                break
            else:
                print("You want to take another card : yes or no ")
                x = Error().is_Error()  # need to be yes or no
                if x == "yes":
                    random_choice = random.choices(
                        card_in_game.cards)  # random ...[('3', 'Hearts')]....
                    card_in_game.Deck_pop(
                        card_in_game.find_idx(random_choice[0])
                    )  # pop obj in card_in_game by idx
                    player.add_card(random_choice, card_in_game.cart[
                        random_choice[0][0]])  # add card to player
                    print("~ Player Hand  ~")
                    print("~~~~~~~~~~~~~~~~")
                    Beautiful_printing().Hand_printing(
                        player)  # print 2 card in player hand
                else:
                    print("~ Dealer Hand  ~")
                    print("~~~~~~~~~~~~~~~~")
                    Beautiful_printing().Hand_printing(dealer)
                    for_loop_2 = player.hand_win()
                    break

        while (for_loop_2 == "Go on"):  #if player dont win or lose Dealer move

            if (dealer.hand_win() == "Win"):
                print("Dealer Win")
                player_Chips.lose_bet(y)
                break

            elif (dealer.hand_win() == "Lose"):
                print("Dealer Lose")
                player_Chips.win_bet(y)
                break

            elif (dealer.value < 17):  # 17 > dealer  , dealer +1 card
                random_choice = random.choices(
                    card_in_game.cards)  # random ...[('3', 'Hearts')]....
                card_in_game.Deck_pop(card_in_game.find_idx(
                    random_choice[0]))  # pop obj in card_in_game by idx
                dealer.add_card(random_choice, card_in_game.cart[
                    random_choice[0][0]])  # add card to player
                print("~ Dealer Hand  ~")
                print("~~~~~~~~~~~~~~~~")
                Beautiful_printing().Hand_printing(dealer)

            elif (dealer.value >= 17
                  and dealer.value > player.value):  #    17 <= dealer > player
                print("Dealer Win")
                player_Chips.lose_bet(y)
                break
            else:  # 17 < = dealer < player or  dealer == player
                print("Player Win")
                player_Chips.win_bet(y)
                break

        if (player_Chips.total == 0):
            print("you have 0 Chips !! sorry Game over !! :( ")
            break

        print("You'll want a new game : yes  / no ")
        x = Error().is_Error()  # need to be yes or no
        if x == "no":
            print("Game End")
            print("you have {} Chips in the End of the Game ".format(
                player_Chips.total))
            break
        else:
            print(" ")  # \n
            print(" New Game ")
            print(" ")  # \n
