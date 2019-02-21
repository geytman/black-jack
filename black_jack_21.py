'''
    Welcome to BlackJack! Get as close to 21 as you can without going over! 
    Dealer hits until she reaches 17 . Aces count as 1 or 11
    At first player have 100 Chips , Game Over if player have 0 Chips Or When player Decides to leave

'''

import random
from Card import Card
from Deck import Deck
from Hand import Hand
from Hand import Beautiful_printing
from Error import Error
from Chips import Chips

# GAMEPLAY!
if __name__ == "__main__":
 
    player_Chips = Chips()
    print("Welcome to BlackJack!")

    while (True):
        print("How many chips would you like to bet? you have now {} ".format(
            player_Chips.total))

        # if y is int  , and you have Enough Chips to Play
        y = Error().Error_bet(player_Chips.total)
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
        # random ...[('3', 'Hearts')]....
        random_choice = random.choices(card_in_game.cards)

        card_in_game.Deck_pop(card_in_game.find_idx(
            random_choice[0]))  # pop obj in card_in_game by idx
        player.add_card(
            random_choice,
            card_in_game.cart[random_choice[0][0]])  # add card to player
        #  2 card to player
        # random ...[('3', 'Hearts')]....
        random_choice = random.choices(card_in_game.cards)

        # pop obj in card_in_game by idx
        card_in_game.Deck_pop(card_in_game.find_idx(random_choice[0]))

        # add card to player
        player.add_card(random_choice, card_in_game.cart[random_choice[0][0]])
        print("~ Player Hand  ~")
        print("~~~~~~~~~~~~~~~~")

        # print 2 card in player hand
        Beautiful_printing().Hand_printing(player)

        # win , lose or go on
        for_loop_2 = player.hand_win()

        # player win or not , if not player can take another card
        while (True):
            if (player.hand_win() == "Win"):
                print("player Win")
                for_loop_2 = player.hand_win()
                player_Chips.add(y)
                break

            elif (player.hand_win() == "Lose"):
                print("player Lose")
                for_loop_2 = player.hand_win()
                player_Chips.remove(y)
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
                player_Chips.remove(y)
                break

            elif (dealer.hand_win() == "Lose"):
                print("Dealer Lose")
                player_Chips.add(y)
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
                player_Chips.remove(y)
                break
            else:  # 17 < = dealer < player or  dealer == player
                print("Player Win")
                player_Chips.add(y)
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
