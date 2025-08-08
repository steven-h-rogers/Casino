from CardUtils.Card import Card
from CardUtils.Ace import Ace
from CardUtils.FaceCard import FaceCard

def create_card(face_value, suit, is_face_up=True):
    if face_value == "A":
        return Ace(suit, is_face_up)
    elif face_value in ["J", "Q", "K"]:
        return FaceCard(face_value, suit, is_face_up)
    else:
        try:
            actual_value = int(face_value)
            return Card(face_value, actual_value, suit, is_face_up)
        except ValueError:
            raise ValueError(print(f"Invalid Face Value: {face_value}"))