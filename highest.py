from deck import Deck

class Highest:
    def __init__(self, score, winning_score):
        self.score = score
        self.winning_score = winning_score
        self.deck = Deck()
        self.deck.shuffle()

        self.player_1_score = 0
        self.player_2_score = 0

        self.player_1_turn = True

    def next_turn(self):
        player_1_card = self.deck.draw_card()
        player_2_card = self.deck.draw_card()
        print(f"Player 1 card: {player_1_card.show_string()}")
        print(f"Player 2 card: {player_2_card.show_string()}")

        if player_1_card.num_value > player_2_card.num_value:
            self.player_1_score += self.score
            print("Player 1 wins!")
        elif player_1_card.num_value < player_2_card.num_value:
            self.player_2_score += self.score
            print("Player 2 wins!")
        elif player_1_card.num_suit > player_2_card.num_suit:
            self.player_1_score += self.score
            print("Player 1 wins!")
        elif player_1_card.num_suit < player_2_card.num_suit:
            self.player_2_score += self.score
            print("Player 2 wins!")

        print("====================")

        if not self.check_win():
            self.next_turn()


    def check_win(self):
        if self.player_1_score >= self.winning_score:
            print("Player 1 is the winner!")
            return True
        if self.player_2_score >= self.winning_score:
            print("Player 2 is the winner!")
            return True
        return False
        




