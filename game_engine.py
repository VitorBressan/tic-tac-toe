

class GameEngine():
    def __init__(self):
        # Array that represents the game board slots
        self.board: list[str] = ["","","","","","","","",""]
        self.playerA_name: str = ""
        self.playerB_name: str = ""
        self.current_player: str = ""

    # Method responsible for rendering the game board
    def render_board(self):

        # Function responsible for rendering the apropriate value for the current board slot
        def print_slot_content(slot: str, index: int):
            if slot != "":
                print(f" {slot} ", end="")
            else:
                print(f" {index + 1} ", end="")

        # Function responsible for rendering the sections divisors of the board
        def print_board_sections(cont):
            if cont % 3 != 0:
                    print("|", end="")
            else:
                print("")
                if cont < 7:
                    print("-" * 12)

        cont: int = 0
        for index, slot in enumerate(self.board):
            cont += 1

            print_slot_content(slot, index)
            print_board_sections(cont)

    # Method responsible for rendering the game main screen
    def start_game(self):
        print("""
                -----------
                TIC TAC TOE
                -----------
        """)
        start = input('Want to play ? ("Yes" to play, "No" to exit): ').strip().upper()
        if start == "YES":
            return True
        return False
    
    def is_valid_move(self, move):
        if self.board[move - 1] != "":
            return False
        return True

    #Method that register the name of the current players
    def get_names(self):
        self.playerA_name = input("Type the first player name: ").strip().lower().capitalize()
        self.playerB_name = input("Type the second player name: ").strip().lower().capitalize()
        self.current_player = self.playerA_name

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
        if self.board[0] == self.board[1] == self.board[3] and self.board[0] != "":
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