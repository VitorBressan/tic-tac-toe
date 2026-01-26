from tictactoe.game_engine import GameEngine

nameA = "Player A"
nameB = "Player B"
def test_game_starts_with_empty_board():
    game = GameEngine(nameA, nameB)
    assert game.board == ["", "", "", "", "", "", "", "", ""]

def test_invalid_move_being_made():
    game = GameEngine(nameA, nameB)
    game.board = ["X", "", "", "", "", "", "", "", ""]
    resp = game.make_move(1)
    assert resp == False


def test_valid_move_being_made():
    game = GameEngine(nameA, nameB)
    game.board = ["", "", "", "", "", "", "", "", ""]
    resp = game.make_move(1)
    assert resp == True

def test_check_for_win():
    game = GameEngine(nameA, nameB)
    game.moves_done[nameA] = [4, 5, 6]
    resp = game.check_for_win()
    assert resp == True

def test_switch_player():
    game = GameEngine(nameA, nameB)
    assert game.current_player == nameA
    game.switch_player()
    assert game.current_player == nameB