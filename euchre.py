from deck import Deck

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

        cards = []

        for hand in self.hands:
            cards.append(self.choose_card(hand))

        for card in cards:
            print(card.show_string())

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
        print(f"Player {player}'s hand is: ")
        for card in self.hands[player]:
            if card != None:
                print(card.show_string())
            else:
                print("No card")

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


