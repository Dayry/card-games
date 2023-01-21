def choose_trump(num_players, dealer, flipped):
    pick_up = order_pick_up(num_players, dealer, flipped)
    if pick_up > 0:
        return pick_up, None # This player chose to order the dealer up

    # No one wanted to order the dealer up
    player_made, new_suit = make_trump(num_players, dealer, flipped.suit)
    if player_made > 0:
        return player_made, new_suit # This player made it this suit
    
    return -1, None # No one made it



"""
Given an array of players and the int of the current dealer, asks
each player if they want to order up the dealer. Returns the int of player
that orders or -1 if no one did.
"""
def order_pick_up(num_players, dealer, flipped):
    asked = 0
    current = dealer  + 1

    if current > num_players:
        current = 1

    while asked < num_players:
        if not ask_pick_up(current, flipped):
            current += 1
            asked += 1
            if current > num_players:
                current = 1
        else:
            return current
    return -1

"""
Gets a yes or no from the current player. Returns True for yes and False for no.
"""
def ask_pick_up(player, flipped):
    print(f"Asking player {player}")
    while True:
        player_input = input("Do you want to order up? y/n: ")
        if player_input.lower() != "y" and player_input.lower() != "n":
            print("y or n")
            continue
        else:
            return player_input.lower() == "y"

    return False

"""
Given an array of players and the int of the current dealer, asks
each player if they want to make the trump suit. Returns the int of player
that orders and their chosen suit, or -1 and None if no one did.
"""
def make_trump(num_players, dealer, old_trump):
    asked = 0
    current = dealer  + 1

    if current > num_players:
        current = 1

    while asked < num_players:
        make, suit = ask_make_trump(current, old_trump)
        if not make:
            current += 1
            asked += 1
            if current > num_players:
                current = 1
        else:
            return current, suit
    return -1, None

"""
Gets a yes or no from the current player if they want to make the trump suit. 
Returns True and chosen suit for yes, False and None for no.
"""
def ask_make_trump(player, old_trump):
    print(f"Asking player {player}")
    print(f"Old trump suit was {old_trump}")
    while True:
        player_input = input("Do you want to make the Trump Suit? y/n: ")
        if player_input.lower() != "y" and player_input.lower() != "n":
            print("y or n")
            continue
        else:
            if player_input.lower() == "n":
                return False, None
            else: # Yes
                return True, choose_trump_suit(old_trump)

    return False, None

"""
returns a string of the suit the player chose.
"""
def choose_trump_suit(old_trump):
    while True:
        player_input = input("Enter a suit (spades, clubs, hearts, diamonds): ")
        lower_input = player_input.lower()
        if lower_input == old_trump:
            print("New suit cannot be the same as the old one.")
            continue
        if lower_input == "spades":
            return "spades"
        elif lower_input == "clubs":
            return "clubs"
        elif lower_input == "hearts":
            return "hearts"
        elif lower_input == "diamonds":
            return "diamonds"
        else:
            print("Invalid option")
        