from .DeckUtils.StandardDeck import StandardDeck
standard_deck = StandardDeck()
print(standard_deck)
print(type(standard_deck.deck_counts))
print(standard_deck.deck_counts.items())

for card in standard_deck.live_deck:
    print(card)