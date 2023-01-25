from start_match import start_match

def euchre(num_players, winning_points=11):
    dealer = 1

    scores, opponent = start_match(num_players, dealer)
    print(scores)
    print(opponent)