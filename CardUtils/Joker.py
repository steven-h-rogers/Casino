from .Card import Card

class Joker(Card):

    def __init__(self, is_face_up):
        self.suit = None
        self.face_value = "Joker"
        self.actual_value = "Joker"
        self.is_face_up = is_face_up
