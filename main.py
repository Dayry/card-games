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
        player_hands[dealer] = dealer_pick_up(player_hands[dealer], flipped_card)
    else:
        print(f"Player {player_made} made trumps {trumps}")

    player_hands = change_jack_value(player_hands, trumps, num_players)

    

    new_round(player_hands, num_players, trumps, dealer)

    # Test order pick up
    # print(f"Dealer: {1}")
    # print(order_pick_up(num_players, 1, flipped_card))

    # Test choose trumps
    

    # player_made, suit = make_trump(num_players, 1, "hearts")
    # print(f"Player {player_made} made trumps: {suit}")

    

    # to do:
    # move some fucntions around, change file names
    # track each round winner
    # remove the played card from players hands
    # impliment match (5 rounds)



    # test for get_user_card()
    # index = get_user_card(hands[1], 1)
    # print(hands[1][index].show_string())

def change_jack_value(player_hands, new_suit, num_players):
    left_bower = None
    new_suit = new_suit.lower()
    if new_suit == "diamonds":
        left_bower = "hearts"
    elif new_suit == "hearts":
        left_bower = "diamonds"
    elif new_suit == "spades":
        left_bower = "clubs"
    elif new_suit == "clubs":
        left_bower = "spades"

    for player in range(1, num_players + 1):
        for card_i in range(0, 5):
            card = player_hands[player][card_i]
            # Left bower
            if card.suit.lower() == left_bower and card.num_value == 11:
                player_hands[player][card_i].num_value = 15
            # Right bower
            if card.suit.lower() == new_suit and card.num_value == 11:
                player_hands[player][card_i].num_value = 16
    
    return player_hands


def print_hands(num_players, player_hands, flipped_card):
    for player in range(1, num_players + 1):
        print(f"Player {player}'s hand:")
        for card in range(0, 5):
            print(player_hands[player][card].show_string())
        print("==========")
    print(f"Flipped card: {flipped_card.show_string()}")
    print("==========")

def dealer_pick_up(hand, flipped_card):
    count = 1
    for i in range(0, 5):
        print(f"{count}: {hand[i].show_string()}")
        count += 1
    
    while True:
        player_input = input(f"Choose a card to replace with: {flipped_card.show_string()}:")
        try:
            int(player_input)
        except:
            print("Enter a number")
            continue
        if int(player_input) < 1 or int(player_input) > 5:
            print("Enter a valid index")
            continue
        if hand[int(player_input) - 1] == None:
            print("Enter a valid index")
            continue

        hand[int(player_input) - 1] = flipped_card
        return hand


main()