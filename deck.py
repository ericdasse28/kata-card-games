from card import Card, Rank, Suit


class Deck:
    def __init__(self):
        self.cards = []
        list_suits = [suit for suit in Suit]
        list_ranks = [rank for rank in Rank]

        for suit in list_suits:
            for rank in list_ranks:
                card = Card(suit=suit, rank=rank)
                self.cards.append(card)
