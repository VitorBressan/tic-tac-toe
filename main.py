from game_engine import GameEngine

game = GameEngine()

if game.start_game():
    game.get_names()
    game.render_board()
    
    while True:

        
