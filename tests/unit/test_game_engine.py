from tictactoe.game_engine import GameEngine
import pytest

nameA = "Player A"
nameB = "Player B"

@pytest.fixture
def game():
    return GameEngine(nameA, nameB)

def test_game_starts_with_empty_board(game):
    assert game.board == [""] * 9

def test_invalid_move_being_made(game):
    game.board = ["X"] * 9
    resp = game.make_move(0)
    assert resp == False 

def test_valid_move_being_made(game):
    game.board = [""] * 9
    resp = game.make_move(0)
    assert resp == True

def test_detect_winner(game):
    game.moves_done[nameB] = {3, 4, 5}
    resp = game.detect_winner()
    assert resp == nameB

def test_switch_player(game):
    assert game.current_player == nameA
    game.switch_player()
    assert game.current_player == nameB
    game.switch_player()
    assert game.current_player == nameA

@pytest.mark.parametrize("combo", [
    {0, 1, 2}, {3, 4, 5}, {6, 7, 8},
    {0, 3, 6}, {1, 4, 7}, {2, 5, 8},
    {0, 4, 8}, {2, 4, 6}
])
def test_detect_win_all_combinations(combo, game):
    game.moves_done[nameA] = combo
    resp = game.detect_winner()
    assert resp == nameA

@pytest.mark.parametrize("combo", [
    {0, 1}, 
    {1, 0, 7}, 
    {2, 3, 8}, 
    {1, 1, 1}, 
    {0, 1, 3}, 
    {}
])
def test_not_win_situations(combo, game):
    game.moves_done[nameA] = combo
    resp = game.detect_winner()
    assert resp is None

def test_check_for_draw(game):
    game.board = ["a"] * 9
    resp = game.check_for_drawn()
    assert resp == True

def test_check_game_status_ongoing(game):
    resp = game.check_game_status()
    assert resp[0] == 'ongoing'

def test_check_game_status_draw(game):
    game.board = ["a"] * 9
    resp = game.check_game_status()
    assert resp[0] == 'draw'

def test_check_game_status_win(game):
    game.moves_done[nameA] = {0, 4, 8}
    resp = game.check_game_status()
    assert resp == ('win', nameA)

def test_win_has_priority_over_draw(game):
    # Simula board cheio
    game.board = ["a"] * 9
    
    # Simula vitória existente
    game.moves_done[nameA] = {0, 4, 8}

    assert game.check_game_status() == ("win", nameA)

def test_mark_slot(game):
    resp = game.mark_slot()
    assert resp == "X"
    game.switch_player()
    resp = game.mark_slot()
    assert resp == "O"

def test_is_valid_mode(game):
    resp = game.is_valid_move(-1)
    assert resp is False

    resp = game.is_valid_move(5)
    assert resp is True