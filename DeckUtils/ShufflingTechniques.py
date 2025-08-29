import typing
import random

def wash(deck):
    random.shuffle(deck)
    return deck

def distributiveRiffle(half1, half2):
    pass

""" allow the user to either submit an index or percentage. Percentages get
recursively forced into indeces"""
def cut(deck, index=None, percentage=.50):
    if index is not None:
        half1, half2 = deck[0:index:1], deck[index:-1:1]
        deck = half2 + half1
        return deck
    else:
        index = int(len(deck)*percentage)
        return cut(deck, index=index)


    
""" determine by random whether there will be 5 or 6 cuts
divide the deck length by the amount of cuts to get a baseline number of cards per cut
randomly add or subtract [0-4] cards per stack except for the last one which will just
be however many cards are there
rearrange the deck where the bottom stack ends up on top and the top stack ends
up on the bottom
"""
def stip_shuffle(deck):
    pass