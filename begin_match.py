# Match is 5 rounds
# round 5 turns, one each player
# Turn one person play a card

def round(player_hands, trumps, dealer):
    pass


def turn():
    pass

    """
Given an array of Cards, shows them to the user and returns the index of the
card they chose.
"""
def get_user_card(hand, player):
    count = 1
    print(f"Player {player}'s hand is: ")
    for card in hand:
        if card != None:
            print(f"{count}:{card.show_string()}")
        else:
            print(f"{count}:No card")
        count += 1
            
    while True:
        player_input = input("Enter a card index:")
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

        # Note the list is from 1 to 5 but the actual index is 0-4
        # this returns the actual index
        return int(player_input) - 1
