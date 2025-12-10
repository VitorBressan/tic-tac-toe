

class GameEngine():
    def __init__(self):
        # Array that represents the game board slots
        self.board: list[str] = ["","","","","","","","",""]
        self.playerA_name: str = ""
        self.playerB_name: str = ""
        self.current_player: str = ""
        print("""
                -----------
                TIC TAC TOE
                -----------
        """)

    # Function responsible for rendering the game board
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

    # Function responsible for rendering the game main screen
    def start_game(self):
        start = input('Want to play ? ("Yes" to play, "No" to exit): ').strip().upper()
        if start == "YES":
            return True
        return False
    
    def verify_move(self, move):
        if self.board[move - 1] != str(move):
            return False
        return True

    #Procedure that register the name of the current players
    def get_names(self):
        self.playerA_name = input("Type the first player name: ").strip().lower().capitalize()
        self.playerB_name = input("Type the second player name: ").strip().lower().capitalize()
        self.current_player: str = self.playerA_name

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
        
    def make_move(self):
        move = int(input(f"{self.current_player} where do you want to play ?"))
        if self.verify_move(move):
            self.board[move - 1] = self.mark_slot()
            self.switch_player()
        else:
            print("Please choose a valid slot!")
            self.make_move()