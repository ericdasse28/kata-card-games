from card import Card, Rank, Suit


def test_can_create_a_card():
    card = Card(suit=Suit.SPADE, rank=Rank.ACE)

    assert card.suit == Suit.SPADE
    assert card.rank == Rank.ACE
