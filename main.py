from set_up import set_up

def main():
    num_players = 3
    player_hands, flipped_card = set_up(num_players)

    # Deal
    for player in range(1, num_players + 1):
        print(f"Player {player}'s hand:")
        for card in range(0, 5):
            print(player_hands[player][card].show_string())
        print("==========")
    print(f"Flipped card: {flipped_card.show_string()}")

    

    # to do:
    # Trump.py
    # - order up each player
    # - make trump each player
    # - reset
    # begin match
    # get get_user_card goes here somewhere

    # test for get_user_card()
    # index = get_user_card(hands[1], 1)
    # print(hands[1][index].show_string())
    

main()