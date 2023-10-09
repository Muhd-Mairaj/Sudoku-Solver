"""
Working no numpy solution
Much faster, added optimisations.

Tests for most functions in test_main.py
"""

from Resources.resources import SOLVED, BOARD
from Resources.resources import displayed, display
import time


def get_subpart_index(i, j):
    """
    i: row index
    j: col index
    
    Formula:
    - x // 3 gives score from 0-2
    - Multiply row score by 3 to add weight
    - Finally sum with col score to get subpart index

    returns: the index of 3x3 subpart which encapsulates the position [i][j] in sudoku board
    """
    return 3 * (i//3) + j//3


def get_subpart(board, i, j):
    """
    board: the current sudoku board
    i: row index
    j: col index

    returns the relevant 3x3 subpart of board that encapsulates the position board[i][j]
    """
    all_subparts = []
    ind = get_subpart_index(i, j)

    for x in range(0,9,3):
        for j_ in range(0,9,3):
            part = []
            for i_ in range(x,x+3):
                part.append(board[i_][j_:j_+3])
            all_subparts.append(part)
    
    return all_subparts[ind]


def get_row_col(board, i, j):
    """
    board: the current sudoku board
    row: row index
    col: col index

    returns: the row and column in board where row index is i and column index is j
    """
    row = board[i][:]
    col = [board[x][j] for x in range(9)]

    return row, col
    

def is_valid(option, row, col, subpart):
    """
    option: the digit to check for
    row (list): the current row to check option in
    col(list): the current col to check option in
    subpart: the relevant 3x3 subpart to check option in

    Checks board to see if option is a valid choice.
    
    returns: True if option is valid else False
    """
    if option in row or option in col:
        return False
    
    if any(option in sub for sub in subpart):
        return False
    
    return True


def solve(board, i, j):
    if board[i][j] == 0:
        row, col = get_row_col(board, i, j)
        subpart = get_subpart(board, i, j)
        for option in {1, 2, 3, 4, 5, 6, 7, 8, 9}:
            # if option is valid, play the option
            if is_valid(option, row, col, subpart):
                board[i][j] = option

                # base case, if last position, return True
                if i == 8 and j == 8:
                    return True

                # if recurisve call returns True (solved), return True; else continue
                if j == 8:
                    if solve(board, i + 1, 0):
                        return True
                else:
                    if solve(board, i, j+1):
                        return True
        
        # if solution was not found, reset current position return False
        board[i][j] = 0
        return False
    
    elif i == 8 and j == 8:
        return True
    elif j == 8:
        return solve(board, i + 1, 0)
    else:
        return solve(board, i, j+1)


def main():
    display(SOLVED)
    print("------------------------------------")
    
    start = time.time()
    solve(BOARD, 0, 0)
    end = time.time()

    display(BOARD)
    print("------------------------------------")

    display(SOLVED)

    print(SOLVED == BOARD)
    interval = end - start
    print("Total time taken to solve the puzzle was:", interval)
    
    
    
if __name__ == '__main__':
    main()
