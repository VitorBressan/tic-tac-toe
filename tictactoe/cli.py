import os

from .game_engine import GameEngine

BOARD_SIZE = 9
MIN_POSITION = 1
MAX_POSITION = BOARD_SIZE


def clear_terminal() -> None:
    """Clears the terminal"""
    os.system("cls" if os.name == "nt" else "clear")


def get_board_index_from_input() -> int:
    """Ask the player where he wants to play and returns a valid 0-based answear."""
    while True:
        try:
            move = int(input().strip())
        except ValueError:
            print("Please type a number!")
            continue

        if move < MIN_POSITION or move > MAX_POSITION:
            print(f"Please type a number between {MIN_POSITION} and {MAX_POSITION}!")
            continue

        return move - 1


def render_board(board_data: list[str]) -> None:
    """Function responsible for rendering the game board"""

    def print_slot_content(slot: str, index: int) -> None:
        """
        Function responsible for rendering the
        appropriate value for the current board slot.
        """
        if slot != "":
            print(f" {slot} ", end="")
        else:
            print(f" {index + 1} ", end="")

    def print_board_sections(cont: int) -> None:
        """Function responsible for rendering the sections divisors of the board."""
        if cont % 3 != 0:
            print("|", end="")
        else:
            print("")
            if cont < 7:
                print("-" * 12)

    cont = 0
    for index, slot in enumerate(board_data):
        cont += 1
        print_slot_content(slot, index)
        print_board_sections(cont)


# Ask the player if he wants to play the game.
def start_game() -> bool:
    start = input('Want to play ? ("Yes" to play, "No" to exit): ').strip().upper()
    if start == "YES":
        return True
    return False


# Prints the game logo.
def show_game_logo() -> None:
    print("-----------\nTIC TAC TOE\n-----------")


# Update the game interface on the terminal.
def update_game_screen(game_board: list[str]) -> None:
    clear_terminal()
    show_game_logo()
    render_board(game_board)

def run_game() -> None:
    if not start_game():
        return 
    
    show_game_logo()
    player1 = input("Type the first player name: ").strip().lower().capitalize()
    player2 = input("Type the second player name: ").strip().lower().capitalize()
    game = GameEngine(player1, player2)
    while True:
        update_game_screen(game.board)
        print(f"{game.current_player} turn!")
        while True:
            print(f"{game.current_player} where do you want to play ?")
            move = get_board_index_from_input()
            # Cheks if the move is valid in the game context.
            if game.make_move(move):
                break
            else:
                print("Invalid Move! Please choose a valid slot!")
        # Check game status.
        game_status = game.check_game_status()
        match game_status[0]:
            case "win":
                update_game_screen(game.board)
                print(f"CONGRATULATIONS {game_status[1]}! YOU'VE WON!")
                break
            case "draw":
                update_game_screen(game.board)
                print("THE GAME HAS COME TO A DRAW!")
                break
        game.switch_player()
