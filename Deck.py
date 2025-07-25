from collections import defaultdict, Counter, deque
import typing
class Deck:

    STANDARD_SUITS = ("Spades", "Clubs", "Hearts", "Diamonds")
    STANDARD_VALUES = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def __init__(self, num_decks=1):
        self.num_decks = num_decks
        self.deck = defaultdict(Counter)
        all_cards = Deck.STANDARD_VALUES * num_decks

        
        for suit in Deck.STANDARD_SUITS:
            for _ in range(self.num_decks):
                self.deck[suit] = Counter(all_cards)


    def __str__(self):
        deck_metadata = f"This deck uses {self.num_decks} deck{'s' if self.num_decks > 1 else ''}."
        cards_and_counts_by_suit = ""
        total_cards = 0
        for suit in self.deck:
            for card, count in self.deck[suit].items():
                cards_and_counts_by_suit += f"X{count} {card} of {suit}  |"
                total_cards += 1

            cards_and_counts_by_suit += '\n'

        total_cards_string = f"\n\nThere are {total_cards} cards in this deck"
        deck_info = (deck_metadata + cards_and_counts_by_suit + total_cards_string)
        return deck_info
    

standard_deck = Deck()
print(standard_deck)
            


        
        