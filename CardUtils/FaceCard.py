from CardUtils.Card import Card
class FaceCard(Card):

    def __init__(self, face_value, suit, is_face_up=True):
        self.face_value = face_value
        self.actual_value = 10
        self.suit = suit
        self.is_face_up = is_face_up