import random


class Board:
    def __init__(self):
        self.field = [[" " for _ in range(4)] for _ in range(4)]
        self.field[0] = [' ', 'a', 'b', 'c']
        for line in range(1, 4):
            self.field[line][0] = str(line)

    def display(self):
        print("---------")
        for row in self.field:
            print("|" + "|".join(row) + "|")
            print("---------")


class ComputerPlayer:
    def __init__(self, symbol):
        self.symbol = symbol

    def choose_move(self, board):
        self.board = board
        move_complete = False
        while not move_complete:
            column = random.randint(1, 3)
            line = random.randint(1, 3)
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
