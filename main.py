from game_engine import GameEngine

game = GameEngine()

if game.start_game():
    game.get_names()
    
    while True:
        game.render_board()
        print(f"{game.current_player} turn!")
        move_done = False

        while not move_done:
            move = int(input(f"{game.current_player} where do you want to play? "))
            if game.make_move(move):
                move_done = True
            else:
                print("Invalid Move! Please choose a valid slot!")

        game.switch_player()
