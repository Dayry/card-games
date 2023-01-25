from start_match import start_match

"""
Plays a game of euchre.
"""
def euchre(num_players, winning_points=11):
    dealer = 1
    game_scores = {}
    for p in range(1, num_players + 1):
        game_scores[p] = 0

    playing = True
    game_winners = []

    while playing:
        scores, opponent = start_match(num_players, dealer)
        match_winners = check_match_winners(scores, opponent)

        #Distrubute points
        for player in match_winners:
            game_scores[player[0]] += player[1]

        playing, game_winners = check_game_winner(game_scores, winning_points)
        dealer += 1
        if dealer > num_players:
            dealer = 1
    
    for winner in game_winners:
        print(f"Player {winner} has won!")



"""
Checks to see if any players have reached the winning score.
"""
def check_game_winner(game_scores, winning_points):
    winners = []
    playing = True
    for player_i in range(1, len(game_scores) + 1):
        if game_scores[player_i] >= winning_points:
            winners.append(player_i)
            playing = False
    
    return playing, winners

"""
Checks to see how many points each player should get.
"""
def check_match_winners(scores, opponent):
    winners = []
    # Order up/make won
    if scores[opponent] == 3 or scores[opponent] == 4:
        winners.append([opponent, 1])
        return winners
    if scores[opponent] == 5:
        winners.append([opponent, 2])
        return winners
    
    # Order up/make lost, others get points
    for player in range(1, len(scores) + 1):
        if player == opponent:
            continue
        # Player contributed so get 1 point
        if scores[player] > 0:
            winners.append([player, 1])
        # One player beat opponent alone
        if scores[player] == 5:
            return [
                [player, 4]
            ]
    
    return winners