from collections import defaultdict, Counter, deque
from ..CardUtils.CardTemplate import create_card
import typing
class Deck:


    # Constructor (Default uses one deck)
    def __init__(self, suits, face_values, num_decks=1):
        self.num_decks = num_decks
        # deck_counts[suit][face_value] -> count
        self.deck_counts = defaultdict(Counter)
        self.initialize_deck_counts(suits, face_values)
        self.live_deck = self.initialize_live_deck() # This list stores all of the card objects 

    def initialize_deck_counts(self, suit_list, face_value_list):
        for suit in suit_list:
            for value in face_value_list:
                self.deck_counts[suit][value] = self.num_decks

    def initialize_live_deck(self):
        live_deck = []
        for suit, cards_by_count in self.deck_counts.items():
            for face_value, count in cards_by_count.items():
                for _ in range(count):
                    new_card = create_card(face_value,suit)
                    live_deck.append(new_card)
        return live_deck


    def __str__(self):
        deck_metadata = f"This deck uses {self.num_decks} deck{'s' if self.num_decks > 1 else ''}."
        cards_and_counts_by_suit = ""
        total_cards = 0
        for suit in self.deck_counts:
            for card, count in self.deck_counts[suit].items():
                cards_and_counts_by_suit += f"x{count} {card} of {suit}  |"
                total_cards += count

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
    """Riffle shuffle could be based on a normal distribution of cards skipped using
    random. It could also be based on some sort of timing factor. It could also be the 
    result of a multithreading race condition with some random quality and timing applied
    to it."""
    def standard_single_deck_shuffle(self):
        pass
    




            


        
        