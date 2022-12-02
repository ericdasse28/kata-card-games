from enum import Enum


class Suit(Enum):
    SPADE = "spade"
    HEART = "heart"
    DIAMOND = "diamond"
    CLUB = "club"


class Rank(Enum):
    ACE = "ace"
    TWO = "2"
    THREE = "3"
    FOUR = "4"


class Card:
    def __init__(self, suit: Suit, rank: Rank):
        self.suit = suit
        self.rank = rank
