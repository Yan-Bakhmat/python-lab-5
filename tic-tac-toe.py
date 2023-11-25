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

    def make_move(self, board):
        self.board = board
        decoder = {
            'a': 1,
            'b': 2,
            'c': 3
        }
        tester_column = ['a', 'b', 'c']
        tester_lines = ['1', '2', '3']
        move_complate = False
        while not move_complate:
            choose = input("Choose a slot: ")
            if len(choose) == 2 and choose[0] in tester_column and choose[1] in tester_lines and self.board.field[int(choose[1])][decoder[choose[0]]] == ' ':
                self.board.field[int(choose[1])
                                 ][decoder[choose[0]]] = self.symbol
                move_complate = True
            else:
                print('Please select an existing slot')
        return self.board


class EndGame:
    def __init__(self, board):
        pass


board = Board()
board.display()

game_go_on = True


computer = ComputerPlayer('O')
for _ in range(3):
    computer.choose_move(board).display()

human = HumanPlayer('X')
human.make_move(board).display()
