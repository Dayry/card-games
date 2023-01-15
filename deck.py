class Deck:
    def __init__(self):


        

class Card:

    def __init__(self, numSuit, numValue):
        self.numSuit = numSuit
        self.numValue = numValue
        self.suit, self.value = self._getValSuit()

    def _getValSuit(self):
        #clubs diamonds hearts spades
        s = self.numSuit
        v = self.numValue
        suit = 0
        value = 0

        if s == 1:
            suit = "Clubs"
        elif s == 2:
            suit = "Diamonds"
        elif s == 3:
            suit = "Hearts"
        elif s == 4:
            suit = "Spades"
        else:
            suit = "Joker"

        if v == 1:
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
        elif v == 11:
            value = "Jack"
        elif v == 12:
            value = "Queen"
        elif v == 13:
            value = "King"
        else:
            value = "Joker"

        return suit, value

    def showString(self):
        if self.numSuit == 0:
            return "Joker"
        return f"{self.value} of {self.suit}"
