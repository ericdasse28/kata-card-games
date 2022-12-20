import pytest

from model.card import Card, Rank, Suit


@pytest.fixture
def ace_of_spade():
    return Card(Suit.SPADE, Rank.ACE)


@pytest.fixture
def three_of_heart():
    return Card(Suit.HEART, Rank.THREE)


@pytest.fixture
def two_of_diamond():
    return Card(Suit.DIAMOND, Rank.TWO)


@pytest.fixture
def four_of_club():
    return Card(Suit.CLUB, Rank.FOUR)
