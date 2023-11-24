import random


class Board:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]

    def display(self):
        print("-------")
        for row in board:
            print("|" + "|".join(row) + "|")
            print("-------")


class ComputerOlayer:
    def __init__(self, symbol):
        self.symbol = symbol

    def choose_move(self, board):
        pass


class HumanPlayer:
    def __init__(self, symbol):
        self.symbol = symbol

    def make_move(self):
        pass


class EndGame:
    def __init__(self):
        pass


def print_board(board):
    """
    Функція для виведення ігрового поля.
    Матриця 3x3, де кожен елемент - це строка, що представляє клітинку поля:
    " " - пуста клітинка, "X" - хрестик, "O" - нулик.
    """
    print("-------")
    for row in board:
        print("|" + "|".join(row) + "|")
        print("-------")


# Створення пустого поля
board = [[" " for _ in range(3)] for _ in range(3)]

# Виведення пустого поля
print_board(board)