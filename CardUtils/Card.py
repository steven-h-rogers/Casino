"""The card class allows for customization of a deck """

class Card:
    def __init__(self, face_value, actual_value, suit, is_face_up=True):
        self.face_value = face_value
        self.actual_value = actual_value
        self.suit = suit
        self.is_face_up = is_face_up

    def __str__(self):
        return f"{self.face_value} of {self.suit}: value: {self.actual_value}"

#     @classmethod
#     def create(cls, face_value, suit, is_face_up=True):
#         face_value_str = str(face_value).upper()

#         if face_value_str == "A":
#             return Ace(suit, is_face_up)
#         elif face_value_str in ("J", "Q", "K"):
#             return FaceCard(face_value_str, suit, is_face_up)
#         else:
#             try:
#                 value = int(face_value_str)
#                 return cls(face_value_str, value, suit, is_face_up)
#             except ValueError:
#                 raise ValueError(f"Invalid face value: {face_value}")


# ace_diamonds = Card.create("A", "Diamonds")
# ace_clubs = Card.create("A", "Clubs")
# jack_diamonds = Card.create("J", "Diamonds")
# king_diamonds = Card.create("K", "Diamonds")

# print(ace_diamonds, ace_clubs, jack_diamonds, king_diamonds, sep="\n")


