import pytest

from card import Card, Rank, Suit
from deck import Deck
from helpers import LIST_OF_52_CARDS


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


def test_can_create_52_cards_deck():
    list_52_cards = LIST_OF_52_CARDS

    deck = Deck()

    assert len(deck.cards) == 52
    assert deck.cards == list_52_cards
