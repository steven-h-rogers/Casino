from .Deck import Deck

# TODO: Add parameter to change suit names to symbols
class StandardDeck(Deck):

    STANDARD_SUITS = ("Spades", "Hearts", "Clubs", "Diamonds")
    STANDARD_SYMBOLS = ("♠", "♥", "♦", "♣")
    STANDARD_VALUES = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def __init__(self, add_jokers=False):
        super().__init__(StandardDeck.STANDARD_SUITS, StandardDeck.STANDARD_VALUES, num_decks=1)


