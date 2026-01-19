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

game = GameEngine()
if game.start_game():
    game.get_names()
    
    while True:
        game.render_board()
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
