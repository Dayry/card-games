from euchre import *

def main():
    deck = create_deck()
    deck = shuffle_deck(deck)

    num_players = 3

    hands, deck = deal(deck, num_players)

    # test deal()
    # for player in range(1, 4):
    #     print(f"Player {player}'s hand:")
    #     for card in range(0, 5):
    #         print(hands[player][card].show_string())
    #     print("==========")

    # test for get_user_card()
    # index = get_user_card(hands[1], 1)
    # print(hands[1][index].show_string())
    

main()