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

    """
    A round is over when everyones played all 5 of there cards. So all players
    have had 5 turns.
    """
    def new_round(self):
        for p in range(1, self.num_players + 1):
            for i in range(0, 5):
                self.hands[p][i] = self.deck.draw_card().show_string()
        
        self.trump = self.deck.draw_card()

        # go through all players having a turn

    """
    A turn is when one person plays one card
    """
    def next_turn(self, player):


