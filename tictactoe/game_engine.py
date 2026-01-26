

class GameEngine():
    def __init__(self, nameA, nameB):
        # Array that represents the game board slots
        self.board: list[str] = ["","","","","","","","",""]
        self.playerA_name: str = nameA
        self.playerB_name: str = nameB
        self.current_player: str = self.playerA_name
        self.moves_done = {
            self.playerA_name: [],
            self.playerB_name: []
        }

    def is_valid_move(self, move):
        if move < 1 or move > 9:
            return False
        elif self.board[move - 1] != "":
            return False
        return True

    def switch_player(self):
        if self.current_player == self.playerA_name:
            self.current_player = self.playerB_name
        else:
            self.current_player = self.playerA_name

    def mark_slot(self):
        if self.current_player == self.playerA_name:
            return "X"
        else:
            return "O"
        
    def make_move(self, move):
        if self.is_valid_move(move):
            self.board[move - 1] = self.mark_slot()
            self.moves_done[self.current_player].append(move)
            return True
        else:
            return False
    
    def check_for_win(self):
        win_combinations = [
            # lines
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9},
            #columns
            {1, 4, 7},
            {2, 5, 8},
            {3, 6, 9},
            #diagonals
            {1, 5, 9},
            {3, 5, 7}
        ]
        
        for combo in win_combinations:
            if combo.issubset(self.moves_done[self.current_player]):
                return True
        
        return False
        
    def check_for_drawn(self):
        for slot in self.board:
            if slot == "":
                return False

        return True