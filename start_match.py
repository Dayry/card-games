from set_up import set_up, print_hands
from choose_trump import choose_trump
from new_round import new_round

def start_match(num_players, dealer): # remember to set 3, 1 when calling
    # Create deck and shuffle
    # Deal to each player
    # Flip card     
    player_hands, flipped_card = set_up(num_players)
    print_hands(num_players, player_hands, flipped_card)

    # Ask each player if they want to order up
    # 1. Yes -> Begin
    # 2. No
    #   Ask each player they want to make trumps
    #   a. Yes -> Begin
    #   b. No -> Go back to Create
    print(f"Dealer is player {dealer}")
    player_made, trumps = choose_trump(num_players, dealer, flipped_card)

    if player_made < 0: # Reset hands and flipped card
        print("Reset")
        return start_match(num_players, dealer)
    elif trumps == None:
        print(f"Player {player_made} ordered up the dealer")
        trumps = flipped_card.suit
        player_hands[dealer] = dealer_pick_up(player_hands[dealer], flipped_card)
    else:
        print(f"Player {player_made} made trumps {trumps}")

    # Change the value of the jacks for right and left bower
    player_hands = change_jack_value(player_hands, trumps, num_players)


    # play the round
    player_hands, winner = new_round(player_hands, num_players, trumps, dealer)
    print(f"Round 1 winner was player: {winner}")

    print_hands(num_players, player_hands, flipped_card)
    player_hands, winner = new_round(player_hands, num_players, trumps, dealer)
    print(f"Round 2 winner was player: {winner}")



def change_jack_value(player_hands, new_suit, num_players):
    left_bower = None
    new_suit_c = new_suit.lower()
    if new_suit_c == "diamonds":
        left_bower = "hearts"
    elif new_suit_c == "hearts":
        left_bower = "diamonds"
    elif new_suit_c == "spades":
        left_bower = "clubs"
    elif new_suit_c == "clubs":
        left_bower = "spades"

    for player in range(1, num_players + 1):
        for card_i in range(0, 5):
            card = player_hands[player][card_i]
            # Left bower
            if card.suit.lower() == left_bower and card.num_value == 11:
                player_hands[player][card_i].num_value = 15
                player_hands[player][card_i].suit = new_suit
            # Right bower
            if card.suit.lower() == new_suit and card.num_value == 11:
                player_hands[player][card_i].num_value = 16
    
    return player_hands

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



