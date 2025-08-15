from .Deck import Deck

class StandardDeck(Deck):

    STANDARD_SUITS = ("Spades", "Clubs", "Hearts", "Diamonds")
    STANDARD_VALUES = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def __init__(self, add_jokers=False):
        super().__init__(StandardDeck.STANDARD_SUITS, StandardDeck.STANDARD_VALUES, num_decks=1)


