from deck import Deck

def main():
    deck = Deck()

    deck.shuffle()
    print(deck.drawCard().showString())

main()