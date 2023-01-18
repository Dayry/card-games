from deck import Deck
import os

class Euchre:

    def __init__(self, num_players, winning_score=11):
        self.deck = Deck(card_list="euchre")
        self.deck.shuffle()

        self.num_players = num_players
        self.winning_score = winning_score

        self.scores = {}
        
        self.dealer = 1
        self.player = 1
        self.caller = None

        self.hands = {}
        self.trump = None

        for p in range(1, num_players + 1):
            self.scores[p] = 0
            self.hands[p] = [None, None, None, None, None]

        self.new_round()

        
        #print(f"Player {2} chose {self.choose_card(2).show_string()}")


    """
    A round is over when everyones played all 5 of there cards. So all players
    have had 5 turns.
    """
    def new_round(self):
        for p in range(1, self.num_players + 1):
            for i in range(0, 5):
                self.hands[p][i] = self.deck.draw_card()
        
        self.trump = self.deck.draw_card()

        cards = {}
        leading = None
        trump = "spades"
        # When set trump, called set_bower_values() to change the 
        # jacks value to 15 (left) and 16 (right)
        # e.g. jack of clubs would be 15, jack of spaces 16
        #self.set_bower_values("spades")

        for hand in self.hands:
            if leading:
                print(f"Leading suit: {leading}, Trump: {trump}") 
                cards[hand] = self.choose_card(hand)
            else:
                cards[hand] = self.choose_card(hand)
                leading = cards[hand].suit
                print(f"Leading suit is now: {leading}")
            print("==================")

        winning_card, winner = self.round_winner(cards, trump)
        print(f"Player {winner} wins this round with {winning_card.show_string()}")

    def set_bower_values(self, right_bower, left_bower, trump):
        if trump == "clubs": 
            # set jack of clubs values to 16, jack of spades value to 15
            print(self.deck.cards[1][11])
            print(self.deck.cards[4][11])
        elif trump == "diamonds":
            # set jack of diamonds values to 16, jack of hearts value to 15
            print(self.deck.cards[2][11])
            print(self.deck.cards[3][11])
        elif trump == "hearts":
            # set jack of hearts values to 16, jack of diamonds value to 15
            print(self.deck.cards[3][11])
            print(self.deck.cards[2][11])
        else: # set jack of spades values to 16, jack of clubs value to 15
            pass
            #print(self.deck.cards[4][11])
            #print(self.deck.cards[1][11])
    
    def round_winner(self, cards, trump):
        for i in range(1, self.num_players + 1):
            if cards[i].value == "jack" and cards[i].suit == trump:
                card[i].num_value = 16
        # check left bower

        curr_winner_card = cards[1]
        curr_winner = 1
        leading = curr_winner_card.suit
        for i in range(2, self.num_players + 1):
            if curr_winner_card.suit == trump:
                if cards[i].value > curr_winner_card.value:
                    curr_winner_card = cards[i]
                    curr_winner = i
        
        return curr_winner_card, curr_winner
        


    """
    A turn is when one person plays one card
    """
    def next_turn(self, player):
        pass

    def set_trump(self):
        if self.dealer + 1 <= self.num_players:
            pass
        pass

    def choose_card(self, player):
        count = 1
        print(f"Player {player}'s hand is: ")
        for card in self.hands[player]:
            if card != None:
                print(f"{count}:{card.show_string()}")
            else:
                print(f"{count}:No card")
            count += 1

        bad_input = True
        card = None
        while bad_input:
            player_input = input("Enter a card index:")
            try:
                int(player_input)
            except:
                print("Enter a number")
                continue
            if int(player_input) < 1 or int(player_input) > 5:
                print("Enter a valid index")
                continue
            if self.hands[player][int(player_input) - 1] == None:
                print("Enter a valid index")
                continue

            card = self.hands[player][int(player_input) - 1]
            bad_input = False
        return card


