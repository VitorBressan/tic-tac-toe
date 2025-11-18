# Array that represents the game board slots
board: list[str] = ["","","","","","","","",""]

# Function responsible for rendering the apropriate value for the current board slot
def print_slot_content(slot: str, index: int):
    if slot != "":
        print(slot, end="")
    else:
        print(index + 1, end="")

def render_board(board: list):
    cont: int = 0
    for index, slot in enumerate(board):
        cont += 1

        print_slot_content(slot, index)

        if cont % 3 != 0:
            print("/", end="")
        else:
            print("\n")

render_board(board)