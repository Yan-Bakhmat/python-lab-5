import random


class Board:
    def __init__(self):
        self.field = [[" " for _ in range(3)] for _ in range(3)]

    def display(self):
        print("-------")
        for row in self.field:
            print("|" + "|".join(row) + "|")
            print("-------")


class ComputerPlayer:
    def __init__(self, symbol):
        self.symbol = symbol

    def choose_move(self, board):
        self.board = board
        move_complete = False
        while not move_complete:
            column = random.randint(0, 2)
            line = random.randint(0, 2)
            if self.board.field[line][column] == " ":
                self.board.field[line][column] = self.symbol
                move_complete = True
            return self.board


class HumanPlayer:
    def __init__(self, symbol):
        self.symbol = symbol

    def make_move(self):
        pass


class EndGame:
    def __init__(self):
        pass


board = Board()
board.display()

computer = ComputerPlayer('X')
for _ in range(3):
    computer.choose_move(board).display()
