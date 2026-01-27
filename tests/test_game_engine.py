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
    game.current_player = nameA
    resp = game.check_for_win()
    assert resp == True

def test_switch_player():
    game = GameEngine(nameA, nameB)
    assert game.current_player == nameA
    game.switch_player()
    assert game.current_player == nameB

def test_all_horizontal_wins():
    horizontal_win_combos = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    for combo in horizontal_win_combos:
        game = GameEngine(nameA, nameB)
        game.moves_done[game.current_player] = combo
        resp = game.check_for_win()
        assert resp == True

def test_all_vertical_wins():
    vertical_win_combos = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    for combo in vertical_win_combos:
        game = GameEngine(nameA, nameB)
        game.moves_done[game.current_player] = combo
        resp = game.check_for_win()
        assert resp == True
    
def test_all_diagonal_wins():  
    diagonal_win_combos = [[1, 5, 9], [3, 5, 7]]
    for combo in diagonal_win_combos:
        game = GameEngine(nameA, nameB)
        game.moves_done[game.current_player] = combo
        resp = game.check_for_win()
        assert resp == True


def test_not_win_situations():
    not_win_combos = [[1, 2], [2, 1, 8], [3, 4, 9], [2, 2, 2], [1, 2, 4], []]
    for combo in not_win_combos:
        game = GameEngine(nameA, nameB)
        game.moves_done[game.current_player] = combo
        resp = game.check_for_win()
        assert resp == False