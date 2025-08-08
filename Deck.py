from collections import defaultdict, Counter, deque
import CardUtils.CardTemplate as CardTemplate

import typing
class Deck:

    # Constants for initialization of a standard deck
    STANDARD_SUITS = ("Spades", "Clubs", "Hearts", "Diamonds")
    STANDARD_VALUES = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    # Constructor (Default uses one deck)
    def __init__(self, num_decks=1):
        self.num_decks = num_decks
        # deck_counts[suit][face_value] -> count
        self.deck_counts = defaultdict(Counter) # This is the actual live deck that will be used in most operations

        self.initialize_deck_counts()

        self.live_deck = self.initialize_live_deck()


    def initialize_deck_counts(self):
        for suit in Deck.STANDARD_SUITS:
            for value in Deck.STANDARD_VALUES:
                self.deck_counts[suit][value] = self.num_decks

    def initialize_live_deck(self):
        live_deck = []
        for suit, cards_by_count in self.deck_counts.items():
            for face_value, count in cards_by_count.items():
                for _ in range(count):
                    new_card = CardTemplate.create_card(face_value,suit)
                    live_deck.append(new_card)
        return live_deck


    def __str__(self):
        deck_metadata = f"This deck uses {self.num_decks} deck{'s' if self.num_decks > 1 else ''}."
        cards_and_counts_by_suit = ""
        total_cards = 0
        for suit in self.deck_counts:
            for card, count in self.deck_counts[suit].items():
                cards_and_counts_by_suit += f"x{count} {card} of {suit}  |"
                total_cards += 1

            cards_and_counts_by_suit += '\n'

        total_cards_string = f"\n\nThere are {total_cards} cards in this deck"
        deck_info = (deck_metadata + cards_and_counts_by_suit + total_cards_string)
        return deck_info
    
    # Step 1 of a standard shuffling on a single deck
    # Cut the deck into 3-5 sections then reverse the order 
    def strip_cut(self, cut_range = (3,5)):
        pass



    """
    Standard shuffle method for a single deck in casinos
    used for poker and some blackjack games:
    Split the deck into 3-5 roughly equal sections and reverse their order
    (top section will now be bottom, bottom will be top. This gets rid of any
    preexisting sequences and ensures that the deck is fairly shuffles)
    Step 2 is 2-3 riffle shuffles where equal halves are (not perfectly 1-1 interleaved)
    Step3: box shuffle: 4-6 4-6 cards are taken from the top and put underneath in small
    blocks (same purpose as step 1)
    step 4 final riffles: 1-2 more times
    step 5: the player selects where to cut the deck
    """
    def standard_single_deck_shuffle(self):
        pass
    

standard_deck = Deck()
print(standard_deck)
print(type(standard_deck.deck_counts))
print(standard_deck.deck_counts.items())

for card in standard_deck.live_deck:
    print(card)


            


        
        