from .Card import Card
from .Ace import Ace
from .FaceCard import FaceCard
from .Joker import Joker

# TODO: change this to a switch case mayber to make it look cleaner
# maybe even make this a factory pattern
@staticmethod
def create_card(face_value, suit, is_face_up=True):
    if face_value == "A":
        return Ace(suit, is_face_up)
    elif face_value in ["J", "Q", "K"]:
        return FaceCard(face_value, suit, is_face_up)
    elif face_value == "Joker":
        return Joker(is_face_up)
    else:
        try:
            actual_value = int(face_value)
            return Card(face_value, actual_value, suit, is_face_up)
        except ValueError:
            raise ValueError(print(f"Invalid Face Value: {face_value}"))