from tictactoe.game_engine import GameEngine
import pytest

nameA = "Player A"
nameB = "Player B"

@pytest.fixture
def game():
    return GameEngine(nameA, nameB)

def test_full_game_win(game):
    # A
    game.make_move(0)
    assert game.check_game_status() == ("ongoing", None)
    game.switch_player()

    # B
    game.make_move(3)
    assert game.check_game_status() == ("ongoing", None)
    game.switch_player()

    # A
    game.make_move(1)
    assert game.check_game_status() == ("ongoing", None)
    game.switch_player()

    # B
    game.make_move(4)
    assert game.check_game_status() == ("ongoing", None)
    game.switch_player()

    # A - winning move
    game.make_move(2)
    status = game.check_game_status()
    assert status == ("win", nameA)


def test_full_game_draw(game):
    moves = [0,1,2,4,3,5,7,6,8]
    for move in moves:
        game.make_move(move)
        status = game.check_game_status()
        if status[0] != "ongoing":
            break
        game.switch_player()

    assert status == ("draw", None)