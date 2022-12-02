from card import Card, Rank, Suit


class Deck:
    def __init__(self):
        self.cards = [
            # Spade
            Card(suit=Suit.SPADE, rank=Rank.ACE),
            Card(suit=Suit.SPADE, rank=Rank.TWO),
            Card(suit=Suit.SPADE, rank=Rank.THREE),
            Card(suit=Suit.SPADE, rank=Rank.FOUR),
            Card(suit=Suit.SPADE, rank=Rank.FIVE),
            Card(suit=Suit.SPADE, rank=Rank.SIX),
            Card(suit=Suit.SPADE, rank=Rank.SEVEN),
            Card(suit=Suit.SPADE, rank=Rank.EIGHT),
            Card(suit=Suit.SPADE, rank=Rank.NINE),
            Card(suit=Suit.SPADE, rank=Rank.TEN),
            Card(suit=Suit.SPADE, rank=Rank.KING),
            Card(suit=Suit.SPADE, rank=Rank.QUEEN),
            Card(suit=Suit.SPADE, rank=Rank.JACK),
            # Heart
            Card(suit=Suit.HEART, rank=Rank.ACE),
            Card(suit=Suit.HEART, rank=Rank.TWO),
            Card(suit=Suit.HEART, rank=Rank.THREE),
            Card(suit=Suit.HEART, rank=Rank.FOUR),
            Card(suit=Suit.HEART, rank=Rank.FIVE),
            Card(suit=Suit.HEART, rank=Rank.SIX),
            Card(suit=Suit.HEART, rank=Rank.SEVEN),
            Card(suit=Suit.HEART, rank=Rank.EIGHT),
            Card(suit=Suit.HEART, rank=Rank.NINE),
            Card(suit=Suit.HEART, rank=Rank.TEN),
            Card(suit=Suit.HEART, rank=Rank.KING),
            Card(suit=Suit.HEART, rank=Rank.QUEEN),
            Card(suit=Suit.HEART, rank=Rank.JACK),
            # Diamond
            Card(suit=Suit.DIAMOND, rank=Rank.ACE),
            Card(suit=Suit.DIAMOND, rank=Rank.TWO),
            Card(suit=Suit.DIAMOND, rank=Rank.THREE),
            Card(suit=Suit.DIAMOND, rank=Rank.FOUR),
            Card(suit=Suit.DIAMOND, rank=Rank.FIVE),
            Card(suit=Suit.DIAMOND, rank=Rank.SIX),
            Card(suit=Suit.DIAMOND, rank=Rank.SEVEN),
            Card(suit=Suit.DIAMOND, rank=Rank.EIGHT),
            Card(suit=Suit.DIAMOND, rank=Rank.NINE),
            Card(suit=Suit.DIAMOND, rank=Rank.TEN),
            Card(suit=Suit.DIAMOND, rank=Rank.KING),
            Card(suit=Suit.DIAMOND, rank=Rank.QUEEN),
            Card(suit=Suit.DIAMOND, rank=Rank.JACK),
            # Club
            Card(suit=Suit.CLUB, rank=Rank.ACE),
            Card(suit=Suit.CLUB, rank=Rank.TWO),
            Card(suit=Suit.CLUB, rank=Rank.THREE),
            Card(suit=Suit.CLUB, rank=Rank.FOUR),
            Card(suit=Suit.CLUB, rank=Rank.FIVE),
            Card(suit=Suit.CLUB, rank=Rank.SIX),
            Card(suit=Suit.CLUB, rank=Rank.SEVEN),
            Card(suit=Suit.CLUB, rank=Rank.EIGHT),
            Card(suit=Suit.CLUB, rank=Rank.NINE),
            Card(suit=Suit.CLUB, rank=Rank.TEN),
            Card(suit=Suit.CLUB, rank=Rank.KING),
            Card(suit=Suit.CLUB, rank=Rank.QUEEN),
            Card(suit=Suit.CLUB, rank=Rank.JACK),
        ]
