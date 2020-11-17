from math import inf as infinity
from random import choice
from random import seed as randomseed       # Paul Lu
import platform
import time
from os import system

"""
An implementation of Minimax AI Algorithm in Tic Tac Toe,
using Python.
This software is available under GPL license.
Author: Clederson Cruz
Year: 2017
License: GNU GENERAL PUBLIC LICENSE (GPL)

Example:
CCID:  rinehart
ID:    1671709

Weekly assignment #6
"""


class Board:
    def __init__(self):
        self.board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ]
        self.HUMAN = -1
        self.COMP = +1
        return

    def __str__(self):
        print(self.board)
        return

    def __repr__(self):
        return

    def get_human(self):
        return self.HUMAN

    def get_comp(self):
        return self.COMP

    def get_board(self):
        return self.board

    def set_board(self,board):
        self.board = board
        return

    def render(self, c_choice, h_choice):
        """
        Print the board on console
        :param state: current state of the board
        """

        chars = {
            -1: h_choice,
            +1: c_choice,
            0: ' '
        }
        final_str = ""
        str_line = '---------------'

        final_str += '\n' + str_line
        for row in self.get_board():
            for cell in row:
                symbol = chars[cell]
                final_str += (f'| {symbol} |')
            final_str += '\n' + str_line
        return final_str

    def evaluate(self):
        """
        Function to heuristic evaluation of state.
        :param state: the state of the current board
        :return: +1 if the computer wins; -1 if the human wins; 0 draw
        """
        if wins(self.COMP):
            score = +1
        elif wins(self.HUMAN):
            score = -1
        else:
            score = 0

        return score


    def wins(self, player):
        """
        This function tests if a specific player wins. Possibilities:
        * Three rows    [X X X] or [O O O]
        * Three cols    [X X X] or [O O O]
        * Two diagonals [X X X] or [O O O]
        :param state: the state of the current board
        :param player: a human or a computer
        :return: True if the player wins
        """

        state = self.get_board()
        win_state = [
            [state[0][0], state[0][1], state[0][2]],
            [state[1][0], state[1][1], state[1][2]],
            [state[2][0], state[2][1], state[2][2]],
            [state[0][0], state[1][0], state[2][0]],
            [state[0][1], state[1][1], state[2][1]],
            [state[0][2], state[1][2], state[2][2]],
            [state[0][0], state[1][1], state[2][2]],
            [state[2][0], state[1][1], state[0][2]],
        ]
        if [player, player, player] in win_state:
            return True
        else:
            return False


    def game_over(self):
        """
        This function test if the human or computer wins
        :param state: the state of the current board
        :return: True if the human or computer wins
        """
        return wins(self.HUMAN) or wins(self.COMP)


    def empty_cells(self):
        """
        Each empty cell will be added into cells' list
        :param state: the state of the current board
        :return: a list of empty cells
        """
        cells = []

        for x, row in enumerate(self.get_board):
            for y, cell in enumerate(row):
                if cell == 0:
                    cells.append([x, y])

        return cells

    def minimax(self, depth, player):
        """
        AI function that choice the best move
        :param state: current state of the board
        :param depth: node index in the tree (0 <= depth <= 9),
        but never nine in this case (see iaturn() function)
        :param player: an human or a computer
        :return: a list with [the best row, best col, best score]
        """
        if player == COMP:
            best = [-1, -1, -infinity]
        else:
            best = [-1, -1, +infinity]

        if depth == 0 or game_over():
            score = evaluate()
            return [-1, -1, score]

        for cell in empty_cells():
            x, y = cell[0], cell[1]
            self.get_board[x][y] = player
            score = minimax(depth - 1, -player)
            self.get_board[x][y] = 0
            score[0], score[1] = x, y

            if player == self.COMP:
                if score[2] > best[2]:
                    best = score  # max value
            else:
                if score[2] < best[2]:
                    best = score  # min value

        return best

class State:
    def __init__(self):
        self.h_choice = ''  # X or O
        self.c_choice = ''  # X or O
        self.first = ''  # if human is the first
        return

    def __str__(self):
        return

    def __repr__(self):
        return

    def clean(self):
        """
        Clears the console
        """
        # Paul Lu.  Do not clear screen to keep output human readable.
        print()
        return

        os_name = platform.system().lower()
        if 'windows' in os_name:
            system('cls')
        else:
            system('clear')

    def valid_move(self, board, x, y):
        """
        A move is valid if the chosen cell is empty
        :param x: X coordinate
        :param y: Y coordinate
        :return: True if the board[x][y] is empty
        """
        if [x, y] in empty_cells(board):
            return True
        else:
            return False

    def set_move(self, board, x, y, player):
        """
        Set the move on board, if the coordinates are valid
        :param x: X coordinate
        :param y: Y coordinate
        :param player: the current player
        """
        if self.valid_move(x, y):
            board.set_board(board.get_board()[x][y] = player)
            return True
        else:
            return False

    def ai_turn(self, board, c_choice, h_choice):
        """
        It calls the minimax function if the depth < 9,
        else it choices a random coordinate.
        :param c_choice: computer's choice X or O
        :param h_choice: human's choice X or O
        :return:
        """
        depth = len(empty_cells(board))
        if depth == 0 or game_over(board):
            return

        self.clean()
        print(f'Computer turn [{c_choice}]')
        board.render(c_choice, h_choice)

        if depth == 9:
            x = choice([0, 1, 2])
            y = choice([0, 1, 2])
        else:
            move = board.minimax(depth, COMP)
            x, y = move[0], move[1]

        self.set_move(x, y, COMP)
        # Paul Lu.  Go full speed.
        # time.sleep(1)


    def human_turn(self, board, c_choice, h_choice):
        """
        The Human plays choosing a valid move.
        :param c_choice: computer's choice X or O
        :param h_choice: human's choice X or O
        :return:
        """
        depth = len(board.empty_cells())
        if depth == 0 or board.game_over():
            return

        # Dictionary of valid moves
        move = -1
        moves = {
            1: [0, 0], 2: [0, 1], 3: [0, 2],
            4: [1, 0], 5: [1, 1], 6: [1, 2],
            7: [2, 0], 8: [2, 1], 9: [2, 2],
        }

        self.clean()
        print(f'Human turn [{h_choice}]')
        board.render(c_choice, h_choice)

        while move < 1 or move > 9:
            try:
                move = int(input('Use numpad (1..9): '))
                coord = moves[move]
                can_move = self.set_move(coord[0], coord[1], HUMAN)

                if not can_move:
                    print('Bad move')
                    move = -1
            except (EOFError, KeyboardInterrupt):
                print('Bye')
                exit()
            except (KeyError, ValueError):
                print('Bad choice')

    def init_choice(self):
        # Human chooses X or O to play
        while self.h_choice != 'O' and self.h_choice != 'X':
            try:
                print('')
                self.h_choice = input('Choose X or O\nChosen: ').upper()
            except (EOFError, KeyboardInterrupt):
                print('Bye')
                exit()
            except (KeyError, ValueError):
                print('Bad choice')

        # Setting computer's choice
        if self.h_choice == 'X':
            self.c_choice = 'O'
        else:
            self.c_choice = 'X'
        while self.first != 'Y' and self.first != 'N':
            try:
                self.first = input('First to start?[y/n]: ').upper()
            except (EOFError, KeyboardInterrupt):
                print('Bye')
                exit()
            except (KeyError, ValueError):
                print('Bad choice')
        # Human may starts first
    def get_choice(self):
        return [self.h_choice,self.c_choice,self.first]

    def set_human(self, choice):
        self.h_choice = choice

    def set_comp(self, choice):
        self.c_choice = choice

if __name__ == '__main__':
    board = Board()
    state = State()
    """
    Main function that calls all functions
    """
    randomseed(274 + 2020)
    state.clean()
    state.init_choice()
    choices = state.get_choice()
    human = choices[0]
    comp = choices[1]
    first = choices[2]
    state.clean()

    # Main loop of this game
    while len(board.empty_cells()) > 0 and not board.game_over():
        if first == 'N':
            state.ai_turn(board, comp, human)
            first = ''

        state.human_turn(board, comp, human)
        state.ai_turn(board, comp, human)

    # Game over message
    if board.wins(board.get_human):
        state.clean()
        print(f'Human turn [{human}]')
        board.render(comp, human)
        print('YOU WIN!')
    elif board.wins(board.get_comp):
        state.clean()
        print(f'Computer turn [{comp}]')
        board.render(comp, human)
        print('YOU LOSE!')
    else:
        state.clean()
        board.render(comp, human)
        print('DRAW!')
    exit()
