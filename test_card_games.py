import pytest

from model.card import Card, Rank, Suit
from model.deck import Deck
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


def test_can_shuffle_cards():
    deck = Deck()
    initial_cards = deck.cards.copy()

    deck.shuffle()

    assert len(deck.cards) == 52
    assert deck.cards != initial_cards
    for card in LIST_OF_52_CARDS:
        assert card in deck.cards
