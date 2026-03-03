from tictactoe.game_engine import GameEngine

nameA = "Player A"
nameB = "Player B"
def test_game_starts_with_empty_board():
    game = GameEngine(nameA, nameB)
    assert game.board == ["", "", "", "", "", "", "", "", ""]

def test_invalid_move_being_made():
    game = GameEngine(nameA, nameB)
    game.board = ["X", "", "", "", "", "", "", "", ""]
    resp = game.make_move(0)
    assert resp == False

def test_valid_move_being_made():
    game = GameEngine(nameA, nameB)
    game.board = ["", "", "", "", "", "", "", "", ""]
    resp = game.make_move(0)
    assert resp == True

def test_detect_winner():
    game = GameEngine(nameA, nameB)
    game.moves_done[nameA] = {3, 4, 5}
    game.current_player = nameA
    resp = game.detect_winner()
    assert resp == nameA

def test_switch_player():
    game = GameEngine(nameA, nameB)
    assert game.current_player == nameA
    game.switch_player()
    assert game.current_player == nameB

def test_all_horizontal_wins():
    horizontal_win_combos = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    for combo in horizontal_win_combos:
        game = GameEngine(nameA, nameB)
        game.moves_done[nameA] = set(combo)
        resp = game.detect_winner()
        assert resp == nameA

def test_all_vertical_wins():
    vertical_win_combos = [[0, 3, 6], [1, 4, 7], [2, 5, 8]]
    for combo in vertical_win_combos:
        game = GameEngine(nameA, nameB)
        game.moves_done[nameA] = set(combo)
        resp = game.detect_winner()
        assert resp == nameA
    
def test_all_diagonal_wins():  
    diagonal_win_combos = [[0, 4, 8], [2, 4, 6]]
    for combo in diagonal_win_combos:
        game = GameEngine(nameA, nameB)
        game.moves_done[nameA] = set(combo)
        resp = game.detect_winner()
        assert resp == nameA


def test_not_win_situations():
    not_win_combos = [[0, 1], [1, 0, 7], [2, 3, 8], [1, 1, 1], [0, 1, 3], []]
    for combo in not_win_combos:
        game = GameEngine(nameA, nameB)
        game.moves_done[nameA] = set(combo)
        resp = game.detect_winner()
        assert resp == None

def test_check_for_draw():
    game = GameEngine(nameA, nameB)
    game.board = ["a", "a", "a", "a", "a", "a", "a", "a", "a"]
    resp = game.check_for_drawn()
    assert resp == True

def test_check_game_status_ongoing():
    game = GameEngine(nameA, nameB)
    resp = game.check_game_status()
    assert resp[0] == 'ongoing'

def test_check_game_status_draw():
    game = GameEngine(nameA, nameB)
    game.board = ["a"] * 9
    resp = game.check_game_status()
    assert resp[0] == 'draw'

def test_check_game_status_win():
    game = GameEngine(nameA, nameB)
    game.moves_done[nameA] = {0, 4, 8}
    resp = game.check_game_status()
    assert resp == ('win', nameA)

def test_win_has_priority_over_draw():
    game = GameEngine(nameA, nameB)

    # Simula board cheio
    game.board = ["a"] * 9
    
    # Simula vitória existente
    game.moves_done[nameA] = {0, 4, 8}

    assert game.check_game_status() == ("win", nameA)