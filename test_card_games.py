import pytest

from card import Card, Rank, Suit


@pytest.mark.parametrize(
    "suit,rank",
    [
        (Suit.SPADE, Rank.ACE),
        (Suit.HEART, Rank.THREE),
        (Suit.DIAMOND, Rank.TWO),
        (Suit.CLUB, Rank.FOUR),
    ],
)
def test_can_create_a_card(suit, rank):
    card = Card(suit=suit, rank=rank)

    assert card.suit == suit
    assert card.rank == rank
