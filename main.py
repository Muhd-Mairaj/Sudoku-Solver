"""
This is the thing but...
    \t- it doesnt work for some reason
"""

from Resources.resources import SOLVED, BOARD
from Resources.resources import displayed, display
import numpy as np


SOLVED = np.array(SOLVED)
BOARD = np.array(BOARD)

options = set([1, 2, 3, 4, 5, 6, 7, 8, 9])


def get_sub(board, i, j):
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
    if option in board[i] or option in board[:,j]:
        return False

    subpart = get_sub(board, i, j)                      # returns a 3x3 np array
    part = [item for line in subpart for item in line]  # returns a list with all the elems of the 3x3 array above
    if option in part:
        return False

    return True


def solve(board, row, col):
    if board[row][col] == 0:

        for option in options:
            if is_valid(row, col, option):
                board[row][col] = option

                if 0 not in board:
                    return True

                elif col == 8:
                    if solve(board, row+1, 0):
                        return True

                else:
                    if not solve(board, row, col+1):
                        return True

        else:
            board[row][col] = 0
            return False
     
    elif col == 8:
        solve(board, row+1, 0)
    else:
        solve(board, row, col+1)

    
def main(board):
    print(all(x.all()==y.all() for x,y in zip(board, SOLVED)))   # should print False
    
    solve(board, 0, 0)
    display(board)

    print(all(x.all()==y.all() for x,y in zip(board, SOLVED)))   # should print True

    
if __name__ == '__main__':
    main()