import typing
from CardUtils.Card import Card

class Ace(Card):
    def __init__(self, suit, is_face_up=True):
        self.face_value = "A"
        self.actual_value = 11 # default value
        self.suit = suit
        self.is_face_up = is_face_up

    # changes ace value for games where ace has variable actual value
    def toggle_ace_value(self) -> None:
        self.value = 1 if self.value == 11 else 11
        