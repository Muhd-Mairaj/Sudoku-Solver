"""
This is the thing but...
    \t- it doesnt work for some reason
"""

from Resources.resources import SOLVED, BOARD
from Resources.resources import displayed, display
import numpy as np


SOLVED = np.array(SOLVED)
BOARD = np.array(BOARD)

all_parts = [BOARD[i:i+3,j:j+3] for i in range(0,9,3) for j in range(0,9,3)]
rows = [BOARD[i] for i in range(9)]
cols = [BOARD[:,i] for i in range(9)]

options = set([1, 2, 3, 4, 5, 6, 7, 8, 9])


def get_part(i, j):
    if i in (0, 1, 2):
        if   j in (0, 1, 2): return 0
        elif j in (3, 4, 5): return 1
        elif j in (6, 7, 8): return 2

    elif i in (3, 4, 5):
        if   j in (0, 1, 2): return 3
        elif j in (3, 4, 5): return 4
        elif j in (6, 7, 8): return 5

    elif i in (6, 7, 8):
        if   j in (0, 1, 2): return 6
        elif j in (3, 4, 5): return 7
        elif j in (6, 7, 8): return 8


def is_valid(i, j, option):
    if option in rows[i] or option in cols[j]: return False

    k = get_part(i, j)
    if any(option in sub for sub in all_parts[k]): return False

    return True


def solve(board, row, col):
    if all(0 not in line for line in board):
        return True

    if board[row][col] == 0:

        for option in options:
            if is_valid(row, col, option):
                board[row][col] = option

                if all(0 not in line for line in board):
                    return True

                elif col == 8:
                    if not solve(board, row+1, 0):
                        board[row][col] = 0
                    else:
                        return True

                else:
                    if not solve(board, row, col+1):
                        board[row][col] = 0
                    else:
                        return True

        else:
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