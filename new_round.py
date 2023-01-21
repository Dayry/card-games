def new_round(player_hands, num_players, trumps, dealer):
    turns = 1
    curr_player = dealer + 1
    if curr_player > num_players:
        curr_player = 1
    lead_suit = None
    played_cards = {}

    while turns <= num_players:
        print(f"Player: {curr_player}")
        # Will only change if lead_suit was None
        lead_suit, played = turn(player_hands[curr_player], lead_suit)
        #played_cards.append({curr_player: played})
        played_cards[curr_player] = played
        turns += 1
        curr_player += 1
        if curr_player > num_players:
            curr_player = 1
    
    print(f"Round winner was player: {round_winner(played_cards, trumps)}")



def round_winner(played_cards, trumps):
    winner_card = played_cards[1]
    for player in range(1, len(played_cards) + 1):
        curr_card = played_cards[player]
        winner_card = compare_cards(winner_card, curr_card, trumps)

    print(f"WINNER CARD: {winner_card.show_string()}")
    
    # Kind of messy having to find the player when the winning 
    # card is already known
    for player in range(1, len(played_cards) + 1):
        if played_cards[player] == winner_card:
            return player # this is the player who won
    
def compare_cards(lead, played, trumps):
    # Special case: bowers
    # Right bower
    if lead.num_value == 16:
        return lead
    if played.num_value == 16:
        return played
    # Left bower: will win as long as the other wasnt the right bower
    if lead.num_value == 15:
        if played.num_value != 16:
            return lead
        else:
            return played
    
    # 1. lead is trumps
    if lead.suit == trumps:
        # a. played is not trumps -> lead wins
        if played.suit != trumps:
            return lead
        # b. played is trumps -> higher value wins
        else:
            if played.value > lead.value:
                return played
            else:
                return lead
    
    # 2. lead is not trumps
    # a. played is trumps -> played wins
    if played.suit == trumps:
        return played
    # b. played is not trumps
    else:
    #   1. played is not lead -> lead wins
        if played.suit != lead.suit:
            return lead
    #   2. played is lead -> higher value wins
        else:
            if played.value > lead.value:
                return played
            else:
                return lead

def turn(player_hand, lead):
    chosen_card_index = get_user_card(player_hand, lead)

    if not lead: # no lead, so make it
        lead = player_hand[chosen_card_index].suit
    return lead, player_hand[chosen_card_index]

"""
Given an array of Cards, shows them to the user and returns the index of the
card they chose.
"""
def get_user_card(hand, lead):
    count = 1
    print(f"Your hand is: ")
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
        if lead: # if theres a lead suit
            if hand_must_follow(hand, lead): # hand contains the lead suit
                if hand[int(player_input) - 1].suit != lead: # if chosen card isn't the leading suit
                    print("You must follow suit")
                    continue

        # Note the list is from 1 to 5 but the actual index is 0-4
        # this returns the actual index
        print("==========")
        return int(player_input) - 1

def hand_must_follow(hand, lead):
    for card in hand:
        if card.suit == lead:
            return True
    
    return False
