import tkinter as tk
from database import *
import random




class GameBoard(tk.Frame):
    def __init__(self, parent, rows=20, columns=20, size=32, color1="white"):
        """size is the size of a square, in pixels"""

        self.rows = rows
        self.columns = columns
        self.size = size
        self.color1 = color1
        self.letters = LETTERS
        self.players = []

        canvas_width = columns * size
        canvas_height = rows * size

        tk.Frame.__init__(self, parent)
        self.canvas = tk.Canvas(self, borderwidth=5, highlightthickness=0,
                                width=canvas_width, height=canvas_height, background="bisque")
        self.canvas.pack(side="top", fill="both", expand=True, padx=2, pady=2)

        peel = tk.Button(text="Peel", command=self.peel)
        peel.pack(side="right", expand=True, padx=2, pady=2)

        start_game = tk.Button(text="Start Game", command=self.distribute)
        start_game.pack(side="right", expand=True, padx=2, pady=2)

        # this binding will cause a refresh if the user interactively
        # changes the window size
        self.canvas.bind("<Configure>", self.refresh)

    def add_player(self, player):
        self.players.append(player)

    def distribute(self):
        if len(self.players) <= 4:
            n = 21
        elif len(self.players) <= 6:
            n = 15
        else:
            n = 11

        while n > 0:
            n -= 1
            for player in self.players:
                player.draw(self.letters)

    def peel(self):
        # all players draw one card
        if sum(self.letters.values()) > len(self.players):
            for player in self.players:
                player.draw(self.letters)

    def refresh(self, event):
        """Redraw the board, possibly in response to window being resized"""
        xsize = int((event.width - 1) / self.columns)
        ysize = int((event.height - 1) / self.rows)
        self.size = min(xsize, ysize)
        self.canvas.delete("square")
        # for row in range(self.rows):
        #     color = self.color1
        #     for col in range(self.columns):
        #         x1 = (col * self.size)
        #         y1 = (row * self.size)
        #         x2 = x1 + self.size
        #         y2 = y1 + self.size
        #         self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill=color, tags="square")

        # for name in self.pieces:
        #     self.placepiece(name, self.pieces[name][0], self.pieces[name][1])
        self.canvas.tag_raise("piece")
        self.canvas.tag_lower("square")

    def addpiece(self, letter, row=0, column=0):
        x0 = (column * self.size) + int(self.size / 2)
        y0 = (row * self.size) + int(self.size / 2)
        CreateCanvasObject(self.canvas, letter, x0, y0)

    # def placepiece(self, name, row, column):
    #     """Place a piece at the given row/column"""
    #     self.pieces[name] = (row, column)
    #     x0 = (column * self.size)
    #     y0 = (row * self.size)
    #     self.canvas.coords(name, x0, y0)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Homebrew Bananagrams")
    game = GameBoard(root)
    game.pack(side="top", fill="both", expand="true", padx=4, pady=4)
    game.add_player(Player("Lyndon"))
    game.addpiece("z", 10, 10)
    game.addpiece("z", 5, 5)
    root.mainloop()