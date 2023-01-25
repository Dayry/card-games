import random

"""
Takes a number of players and returns a hand for each player and a flipped card.
"""
def set_up(num_players):
    deck = create_deck()
    deck = shuffle_deck(deck)

    hands, deck = deal(deck, num_players)
    flipped_card = deck.pop()

    return hands, flipped_card

"""
Prints to console each player and their current hands.
"""  
def print_hands(num_players, player_hands, flipped_card):
    for player in range(1, num_players + 1):
        print(f"Player {player}'s hand:")
        for card in range(0, 5):
            card_to_display = player_hands[player][card]
            if card_to_display:
                print(f"{card}:{card_to_display.show_string()}")
            else:
                print(f"{card}:No card")
        print("==========")
    print(f"Flipped card: {flipped_card.show_string()}")
    print("==========")



"""
Returns an ordered array of Cards making up a euchre deck.
"""
def create_deck():
    deck = []

    for s in range(1, 5): # Suits
        for v in range(7, 15): # Values
            deck.append(Card(s, v))

    return deck

"""
Takes a deck and returns a shuffled copy.
"""
def shuffle_deck(deck):
    random.shuffle(deck)
    return deck

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


class Card:

    def __init__(self, num_suit, num_value):
        self.num_suit = num_suit
        self.num_value = num_value
        self.suit, self.value = self._get_val_suit()

    def _get_val_suit(self):
        s = self.num_suit
        v = self.num_value
        suit = 0
        value = 0

        if s == 1:
            suit = "Hearts"
        elif s == 2:
            suit = "Diamonds"
        elif s == 3:
            suit = "Clubs"
        elif s == 4:
            suit = "Spades"
        else:
            print("Invalid suit number")

        if v == 1 or v == 14:
            value = "Ace"
        elif v == 2:
            value = "Two"
        elif v == 3:
            value = "Three"
        elif v == 4:
            value = "Four"
        elif v == 5:
            value = "Five"
        elif v == 6:
            value = "Six"
        elif v == 7:
            value = "Seven"
        elif v == 8:
            value = "Eight"
        elif v == 9:
            value = "Nine"
        elif v == 10:
            value = "Ten"
        elif v == 12:
            value = "Queen"
        elif v == 13:
            value = "King"
        else: # v == 11 or v == 15 or v == 16+:
            value = "Jack"

        return suit, value

    def show_string(self):
        # Left bower, keep actual suit as trumps, but its 
        # display to its original suit
        if self.num_value == 15:
            display_suit = None
            if self.suit.lower() == "diamonds":
                display_suit = "Hearts"
            elif self.suit.lower() == "hearts":
                display_suit = "Diamonds"
            elif self.suit.lower() == "spades":
                display_suit = "Clubs"
            elif self.suit.lower() == "clubs":
                display_suit = "Spades"
            return f"{self.value} of {display_suit}"

        return f"{self.value} of {self.suit}"