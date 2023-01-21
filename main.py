from set_up import set_up
from choose_trump import choose_trump

from begin_match import *

def main():
    num_players = 3
    player_hands, flipped_card = set_up(num_players)
    print_hands(num_players, player_hands, flipped_card)

    dealer = 1
    print(f"Dealer is player {dealer}")
    player_made, trumps = choose_trump(num_players, dealer, flipped_card)

    if player_made < 0: # Reset hands and flipped card
        print("Reset")
        player_hands, flipped_card = set_up(num_players)
        print_hands(num_players, player_hands, flipped_card)
    elif trumps == None:
        print(f"Player {player_made} ordered up the dealer")
        trumps = flipped_card.suit
    else:
        print(f"Player {player_made} made trumps {trumps}")

    new_round(player_hands, num_players, trumps, dealer)

    # Test order pick up
    # print(f"Dealer: {1}")
    # print(order_pick_up(num_players, 1, flipped_card))

    # Test choose trumps
    

    # player_made, suit = make_trump(num_players, 1, "hearts")
    # print(f"Player {player_made} made trumps: {suit}")

    

    # to do:
    # if ordered to pick up, dealer needs to swap with flipped
    # Change the value and suit of the left bower once trumps is set
    # round winner

    # test for get_user_card()
    # index = get_user_card(hands[1], 1)
    # print(hands[1][index].show_string())

def print_hands(num_players, player_hands, flipped_card):
    for player in range(1, num_players + 1):
        print(f"Player {player}'s hand:")
        for card in range(0, 5):
            print(player_hands[player][card].show_string())
        print("==========")
    print(f"Flipped card: {flipped_card.show_string()}")
    print("==========")


main()