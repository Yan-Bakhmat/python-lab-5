import random


class Board:
    def __init__(self):
        self.field = [[" " for _ in range(4)] for _ in range(4)]
        self.field[0] = [' ', 'a', 'b', 'c']
        for line in range(1, 4):
            self.field[line][0] = str(line)

    def display(self):
        """
        Метод для виведення ігрового поля.
        Матриця 4x4, де перші лінія та стовпчик - це розмітка поля, а всі інші елементи - строки, що представляють клітинки ігрового поля:
        " " - пуста клітинка, "X" - хрестик, "O" - нулик.
        """
        print("---------")
        for row in self.field:
            print("|" + "|".join(row) + "|")
            print("---------")


class ComputerPlayer:
    def __init__(self, symbol):
        self.symbol = symbol

    def choose_move(self, board):
        """
        Метод, що генерує випадковий хід комп'ютера.
        Для покращення логіки вибору клітинк для наступних ходів ком'ютера, в подальшому можна додати алгоритм аналізу ігрового поля, або спрбувати залучити штучний інтилект.
        """
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
        """
        Метод зворотнього зв'язку з гравцем.
        Гравцю пропонується ввести координати поля, куди він хотів би походити, у форматі [літера][цифра].
        Введені дані перевіряються на коректність, у випадку неправильності вводу гравцю надається можливість змінити звій вибір.
        """
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
            choose = input("Choose a free slot: ")
            if len(choose) == 2 and choose[0] in tester_column and choose[1] in tester_lines and self.board.field[int(choose[1])][decoder[choose[0]]] == ' ':
                self.board.field[int(choose[1])
                                 ][decoder[choose[0]]] = self.symbol
                move_complate = True
            else:
                print('Please select a correct slot')
        return self.board


class EndGame:
    def __init__(self):
        """
        Створюється класс, що містить в собі методи для перевірки передумов для завершення гри.
        В подальшому класс можна вдосконалити, щоб він не тільки зберігав їх, а й проводив саму перевірку.
        """
        pass

    def free_slots_exist(self, board):
        """
        Метод перевіряє, чи залишились вільні клітинки на ігровому полі.
        """
        self.board = board
        for n in range(1, 4):
            for k in range(1, 4):
                if board.field[n][k] == ' ':
                    return True
        return False

    def three_in_line(self, board):
        """
        Метод перевіряє ігрове поле на наявність трьох однакових елементів ("X" або "O") по вертикалі, горизонталі чи-то діагоналі.
        """
        self.board = board
        if self.board.field[1][1] == self.board.field[2][2] == self.board.field[3][3] == "O" or self.board.field[1][3] == self.board.field[2][2] == self.board.field[3][1] == "O":
            return True
        elif self.board.field[1][1] == self.board.field[2][2] == self.board.field[3][3] == "X" or self.board.field[1][3] == self.board.field[2][2] == self.board.field[3][1] == "X":
            return True
        else:
            for i in range(1, 4):
                if self.board.field[i][1] == self.board.field[i][2] == self.board.field[i][3] == "O" or self.board.field[1][i] == self.board.field[2][i] == self.board.field[3][i] == "O":
                    return True
                elif self.board.field[i][1] == self.board.field[i][2] == self.board.field[i][3] == "X" or self.board.field[1][i] == self.board.field[2][i] == self.board.field[3][i] == "X":
                    return True
            return False


if __name__ == '__main__':
    board = Board()
    computer = ComputerPlayer('O')
    human = HumanPlayer('X')
    the_end = EndGame()

    game_on = True

    while game_on:
        if the_end.free_slots_exist(board) == True:
            computer.choose_move(board)
            board.display()
            if the_end.three_in_line(board) == False:
                if the_end.free_slots_exist(board) == True:
                    human.make_move(board)
                    board.display()
                    if the_end.three_in_line(board) == True:
                        game_on = False
                        print('You Win!')
            else:
                game_on = False
                print('You Lose')
        else:
            game_on = False
            print('Game Over')
