# Array that represents the game board slots
board: list[str] = ["","","","","","","","",""]

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

# Function responsible for rendering the game board
def render_board(board: list):
    cont: int = 0
    for index, slot in enumerate(board):
        cont += 1

        print_slot_content(slot, index)
        print_board_sections(cont)

# Function responsible for rendering the game main screen
def start_game():
    print("""
            -----------
            TIC TAC TOE
            -----------
    """)
    
    start = input('Want to play ? ("Yes" to play, "No" to exit): ').strip().upper()
    if start == "YES":
        return True
    return False

if start_game():
    render_board(board)

