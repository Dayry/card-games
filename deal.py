"""
Deals 5 cards from the given deck for each number of players and 
returns them in a list, along with the remaining deck.
"""
def deal(deck, num_players):
    # Create empty hands
    hands = {}
    for p in range(1, num_players  + 1):
        hands[p] = [None, None, None, None, None]


    for p in range(1, num_players + 1):
            for i in range(0, 5):
                hands[p][i] = deck.pop()
        
    return hands, deck