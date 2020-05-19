from game_interface import *
from database import *


def start_board():
    root = tk.Tk()
    root.title = "Homebrew Bananagrams"
    board = GameBoard(root)
    board.pack(side="top", fill="both", expand="true", padx=4, pady=4)
    root.mainloop()

# event
# new_game = Game(new_game)
# new_game.add_player("Lyndon")

if __name__ == '__main__':
    start_board()
