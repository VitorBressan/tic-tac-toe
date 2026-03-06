class GameEngine:
    WIN_COMBINATIONS = [
        # lines
        {0, 1, 2},
        {3, 4, 5},
        {6, 7, 8},
        # columns
        {0, 3, 6},
        {1, 4, 7},
        {2, 5, 8},
        # diagonals
        {0, 4, 8},
        {2, 4, 6},
    ]

    def __init__(self, nameA: str, nameB: str):
        # Array that represents the game board slots
        self.board: list[str] = [""] * 9
        self.playerA_name: str = nameA
        self.playerB_name: str = nameB
        self.current_player: str = self.playerA_name
        self.moves_done: dict[str, set[int]] = {
            self.playerA_name: set(),
            self.playerB_name: set(),
        }

    def is_valid_move(self, move: int) -> bool:
        if move < 0 or move >= len(self.board):
            return False
        elif self.board[move] != "":
            return False
        return True

    def switch_player(self) -> None:
        if self.current_player == self.playerA_name:
            self.current_player = self.playerB_name
        else:
            self.current_player = self.playerA_name

    def mark_slot(self) -> str:
        if self.current_player == self.playerA_name:
            return "X"
        else:
            return "O"

    def make_move(self, move: int) -> bool:
        if self.is_valid_move(move):
            self.board[move] = self.mark_slot()
            self.moves_done[self.current_player].add(move)
            return True
        else:
            return False

    def detect_winner(self) -> str | None:
        for combo in self.WIN_COMBINATIONS:
            if combo.issubset(self.moves_done[self.playerA_name]):
                return self.playerA_name
            if combo.issubset(self.moves_done[self.playerB_name]):
                return self.playerB_name
        return None

    def check_for_draw(self) -> bool:
        for slot in self.board:
            if slot == "":
                return False

        return True

    def check_game_status(self) -> tuple[str, str | None]:
        winner = self.detect_winner()
        if winner:
            return ("win", winner)
        if self.check_for_draw():
            return ("draw", None)

        return ("ongoing", None)
