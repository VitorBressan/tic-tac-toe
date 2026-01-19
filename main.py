from game_engine import GameEngine

def ask_for_move():
    valid = False
    while not valid:
        try:
            move = int(input(f"{game.current_player} where do you want to play? ").strip())
        except:
            print("Please type a number from 1 to 9")
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

game = GameEngine()
if game.start_game():
    game.get_names()
    
    while True:
        render_board(game.board)
        print(f"{game.current_player} turn!")
        
        move_done = False
        while not move_done:

            move = ask_for_move()
        
            if game.make_move(move):
                move_done = True
            else:
                print("Invalid Move! Please choose a valid slot!")

        if game.check_for_win():
            print(f"CONGRATULATIONS {game.current_player}! YOU'VE WON!")
            break

        game.switch_player()
