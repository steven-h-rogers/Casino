import numpy as np
import math
# from .Deck import Deck
class Shuffler:

    default_distribution = {1:23, 2:8, 3:3, 4:1}

    def __init__(self):
        total = 0
        for k,v in Shuffler.default_distribution.items():
            total+= k*v
        print(total)
        pass


shuffler = Shuffler()
    