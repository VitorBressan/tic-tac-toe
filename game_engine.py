

class GameEngine():
    def __init__(self):
        # Array that represents the game board slots
        self.board: list[str] = ["","","","","","","","",""]
        self.playerA_name: str = ""
        self.playerB_name: str = ""
        self.current_player: str = ""
    
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
            return True
        else:
            return False
    
    def check_for_win(self):
        #[0][1][2]
        #[3][4][5]
        #[6][7][8]

        # Horizontal Win
        if self.board[0] == self.board[1] == self.board[2] and self.board[0] != "":
            return True
        elif self.board[3] == self.board[4] == self.board[5] and self.board[3] != "":
            return True
        elif self.board[6] == self.board[7] == self.board[8] and self.board[6] != "":
            return True
        
        # Vertical Win
        if self.board[0] == self.board[3] == self.board[6] and self.board[0] != "":
            return True
        elif self.board[1] == self.board[4] == self.board[7] and self.board[1] != "":
            return True
        elif self.board[2] == self.board[5] == self.board[8] and self.board[2] != "":
            return True

        # Diagonal Win
        elif self.board[0] == self.board[4] == self.board[8] and self.board[0] != "":
            return True
        elif self.board[2] == self.board[4] == self.board[6] and self.board[2] != "":
            return True
        
        else:
            return False
        
    def check_for_drawn(self):
        for slot in self.board:
            if slot == "":
                return False
        
        return True