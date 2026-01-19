from game_engine import GameEngine
import os

def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")

def ask_for_move():
    valid = False
    while not valid:
        try:
            move = int(input(f"{game.current_player} where do you want to play? ").strip())
        except ValueError:
            print("Please type a number")
        else:
            valid = True
    return move

# Function responsible for rendering the game board
def render_board(board_data):

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
    for index, slot in enumerate(board_data):
        cont += 1
        print_slot_content(slot, index)
        print_board_sections(cont)

# Function responsible for rendering the game main screen
def start_game():
    start = input('Want to play ? ("Yes" to play, "No" to exit): ').strip().upper()
    if start == "YES":
        return True
    return False

#Function that register the name of the current players
def get_names():
    game.playerA_name = input("Type the first player name: ").strip().lower().capitalize()
    game.playerB_name = input("Type the second player name: ").strip().lower().capitalize()
    game.current_player = game.playerA_name

def show_game_logo():
    print("-----------\nTIC TAC TOE\n-----------")
    
def update_game_screen():
    clear_terminal()
    show_game_logo()
    render_board(game.board)

game = GameEngine()
if start_game():
    show_game_logo()
    get_names()
    
    while True:
        update_game_screen()
        print(f"{game.current_player} turn!")
        
        move_done = False
        while not move_done:

            move = ask_for_move()
        
            if game.make_move(move):
                move_done = True
            else:
                print("Invalid Move! Please choose a valid slot!")

        if game.check_for_win():
            update_game_screen()
            print(f"CONGRATULATIONS {game.current_player}! YOU'VE WON!")
            break
        elif game.check_for_drawn():
            update_game_screen()
            print("THE GAME HAS COME TO A DRAW!")
            break

        game.switch_player()
