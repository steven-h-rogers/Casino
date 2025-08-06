"""The card class allows for customization of a deck """

class Card:
    def __init__(self, face_value, actual_value, suit, is_face_up=True):
        self.face_value = face_value
        self.actual_value = actual_value
        self.suit = suit
        self.is_face_up = is_face_up



