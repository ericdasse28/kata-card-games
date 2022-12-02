from enum import Enum


class Suit(Enum):
    SPADE = "spade"


class Rank(Enum):
    ACE = "ace"


class Card:
    def __init__(self, suit: Suit, rank: Rank):
        self.suit = suit
        self.rank = rank
