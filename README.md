# Euchre

A text based version of the playing card game Euchre.

## Description

Plays a game of euchre with (currently) 4 players who make inputs on the terminal. Its not a very practical way to play but it can serve as the basis for a more user friendly version.

## Getting Started

### Executing program

Currently just runs with main.py
```
python main.py
```
### How to play
* Each player is dealt a hand and a card is flipped.
* This flipped cards suit is "trumps"
* Each player has the option of "ordering up" the dealer, the dealer picks up the card and swaps it with another of their cards, the player that "ordered up" is the "opponent" and must win at least 3 of the 5 turns to win, otherwise any other player that won at least one turn with get a point.
* If no one orders up the dealer (including the dealer) then each player has the option of choosing which suit they want it to be (they cannot chose the suit that was flipped), if they make it they become the "opponent".
* If no one makes it then the deck is shuffled and new hands are dealt and a new card is flipped.
* The player starting at dealer + 1 begins by playing a card.
* Each player follows, the winning card for the turn is either; the highest trump or if there are no trumps then the highest of the suit that was played first.
* The turn winner begins the next turn.

Card values lowest to highest
* 7 to Ace
* But the Jack of the trump suit is the highest value, and the Jack of the same colour suit (i.e if Spades is trumps then Clubs) is the second highest value.
* These are called the Right Bower (same suit trump) and Left Bower (same colour as trump)

Scoring
* Opponent gets 3 or 4 wins: 1 Point
* Opponent gets all 5 wins: 2 Points
* Opponent doesn't get at least 3 wins: each player that got at least 1 win get: 1 Point
* If there was only one player in the above then they get: 2 Points
* One player that isn't the opponent gets all 5 wins: 4 Points

## To do
* Card class has an int representation that isn't used, this would be a lot better than constantly comparing hard coded strings and making sure the case is right for them all.
* The user interface shows all player hands, add in a prompt to make sure only current player is looking at the screen; or just add in a real GUI.
* Make this the basis of a server side program and write a client side program to access this as an API.

## Author
Ryan Day

## Acknowledgments

* [Readme template](https://gist.github.com/DomPizzie/7a5ff55ffa9081f2de27c315f5018afc)


