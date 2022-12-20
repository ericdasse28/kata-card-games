import pytest

from model.player import Player


@pytest.mark.parametrize(
    "name", ("Albert", "Vincent", "Tristan", "Eric", "Léo", "Jacques Chirac", "Hughes")
)
def test_can_create_a_player(name):
    player = Player(name=name)

    assert player.name == name
    assert player.hand is None
