from .game_engine import GameEngine
import os

MIN_POSITION = 1
MAX_POSITION = 9

# Clears the terminal
def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")

# Ask the player where he wants to play and returns a valid 0-based answear.
def get_board_index_from_input():
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

# Function responsible for rendering the game board.
def render_board(board_data):

    # Function responsible for rendering the apropriate value for the current board slot.
    def print_slot_content(slot: str, index: int):
        if slot != "":
            print(f" {slot} ", end="")
        else:
            print(f" {index + 1} ", end="")

    # Function responsible for rendering the sections divisors of the board.
    def print_board_sections(cont):
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
def start_game():
    start = input('Want to play ? ("Yes" to play, "No" to exit): ').strip().upper()
    if start == "YES":
        return True
    return False

# Prints the game logo.
def show_game_logo():
    print("-----------\nTIC TAC TOE\n-----------")

# Update the game interface on the terminal.
def update_game_screen():
    clear_terminal()
    show_game_logo()
    render_board(game.board)


if start_game():
    show_game_logo()
    
    player1 = input("Type the first player name: ").strip().lower().capitalize()
    player2 = input("Type the second player name: ").strip().lower().capitalize()
    game = GameEngine(player1, player2)

    while True:
        update_game_screen()
        print(f"{game.current_player} turn!")
        
        while True:
            print(f"{game.current_player} where do you want to play ?")
            move = get_board_index_from_input()
            # Cheks if the move is valid in the game context.
            if game.make_move(move):
                break 
            else:
                print("Invalid Move! Please choose a valid slot!")

        # Check if the game has ended.
        if game.check_for_win():
            update_game_screen()
            print(f"CONGRATULATIONS {game.current_player}! YOU'VE WON!")
            break
        elif game.check_for_drawn():
            update_game_screen()
            print("THE GAME HAS COME TO A DRAW!")
            break

        game.switch_player()
