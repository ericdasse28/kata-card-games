import pytest

from controller.controller import Controller
from model.player import Player


@pytest.mark.parametrize(
    "card", ["ace_of_spade", "three_of_heart", "two_of_diamond", "four_of_club"]
)
def test_controller_can_distribute_a_card_to_a_player(card, request):
    card = request.getfixturevalue(card)
    player = Player(name="Albert")
    controller = Controller()

    controller.distribute_card(card=card, player=player)

    assert (
        player.hand == card
    ), f"Player hand {player.hand} should not be a card with spade={card.suit} and {card.rank}"
    assert player.hand.face_down
