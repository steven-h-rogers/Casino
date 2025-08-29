# import numpy as np
# import math
from abc import ABC, abstractmethod
# from .Deck import Deck
class Shuffler(ABC):

    # default_distribution: dict = {1:23, 2:8, 3:3, 4:1}

    # def __init__(self):
    #     total = 0
    #     for k,v in Shuffler.default_distribution.items():
    #         total+= k*v
    #     print(total)
    #     pass

    @abstractmethod
    def shuffle(self, deck):
        pass    