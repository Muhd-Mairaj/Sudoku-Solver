# %%
from Resources.resources import SOLVED, BOARD
from Resources.resources import displayed, display
import numpy as np


SOLVED = np.array(SOLVED)
BOARD = np.array(BOARD)
# display(BOARD)

options = set([1, 2, 3, 4, 5, 6, 7, 8, 9])



def get_subpart(board, i, j):
    if i in (0, 1, 2):
        if   j in (0, 1, 2):
            return board[0:3,0:3]
        elif j in (3, 4, 5):
            return board[0:3,3:6]
        elif j in (6, 7, 8):
            return board[0:3,6:9]

    elif i in (3, 4, 5):
        if   j in (0, 1, 2):
            return board[3:6,0:3]
        elif j in (3, 4, 5):
            return board[3:6,3:6]
        elif j in (6, 7, 8):
            return board[3:6,6:9]

    elif i in (6, 7, 8):
        if   j in (0, 1, 2):
            return board[6:9,0:3]
        elif j in (3, 4, 5):
            return board[6:9,3:6]
        elif j in (6, 7, 8):
            return board[6:9,6:9]


def is_valid(board, i, j, option):
    if option in board[i] or option in board[:,j]: return False

    part = [item for sub in get_subpart(board, i, j) for item in sub]
    if option in part: return False

    return True


def solve(board, row, col):

    if all(0 not in line for line in board):
        return True

    if board[row][col] == 0:
        for option in options:
            if is_valid(board, row, col, option):
                board[row][col] = option
                # if all(0 not in line for line in board):
                #     return True

                if col == 8:
                    if solve(board, row+1, 0):
                        return True

                else:
                    if solve(board, row, col+1):
                        return True

        else:
            board[row][col] = 0
            return False
                    
    elif col == 8:
        return solve(board, row+1, 0)
    else:
        return solve(board, row, col+1)


def main(board):
    display(SOLVED)
    print((all(x.all()==y.all() for x,y in zip(board, SOLVED))))
    solve(board, 0, 0)
    display(board)
    print((all(x.all()==y.all() for x,y in zip(board, SOLVED))))


if __name__ == '__main__':
    main(BOARD)
# %%
