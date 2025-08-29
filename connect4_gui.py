# connect4_gui.py

import tkinter as tk
from tkinter import messagebox
import numpy as np
from connect4 import create_board, drop_piece, is_valid_location, get_next_open_row, winning_move

ROWS = 6
COLS = 7
SQUARESIZE = 100
RADIUS = int(SQUARESIZE/2 - 5)

class Connect4:
    def __init__(self, root):
        self.root = root
        self.root.title("Connect 4")
        self.board = create_board()
        self.turn = 0  # Player 1's turn is 0, Player 2's turn is 1
        self.canvas = tk.Canvas(self.root, width=COLS*SQUARESIZE, height=(ROWS+1)*SQUARESIZE, bg="blue")
        self.canvas.pack()
        self.draw_board()
        self.canvas.bind("<Button-1>", self.handle_click)

    def draw_board(self):
        for c in range(COLS):
            for r in range(ROWS):
                x0 = c * SQUARESIZE
                y0 = (r+1) * SQUARESIZE
                x1 = x0 + SQUARESIZE
                y1 = y0 + SQUARESIZE
                self.canvas.create_oval(x0, y0, x1, y1, fill="white")

    def draw_piece(self, row, col, piece):
        color = "red" if piece == 1 else "yellow"
        x0 = col * SQUARESIZE
        y0 = (ROWS-row) * SQUARESIZE
        x1 = x0 + SQUARESIZE
        y1 = y0 + SQUARESIZE
        self.canvas.create_oval(x0, y0, x1, y1, fill=color)

    def handle_click(self, event):
        col = event.x // SQUARESIZE
        if is_valid_location(self.board, col):
            row = get_next_open_row(self.board, col)
            piece = 1 if self.turn == 0 else 2
            drop_piece(self.board, row, col, piece)
            self.draw_piece(row, col, piece)
            if winning_move(self.board, piece):
                winner = "Player 1" if self.turn == 0 else "Player 2"
                messagebox.showinfo("Game Over", f"{winner} wins!")
                self.reset_game()
            self.turn += 1
            self.turn %= 2

    def reset_game(self):
        self.board = create_board()
        self.turn = 0
        self.canvas.delete("all")
        self.draw_board()

if __name__ == "__main__":
    root = tk.Tk()
    game = Connect4(root)
    root.mainloop()
