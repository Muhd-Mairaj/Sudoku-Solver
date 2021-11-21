

BOLD = "\033[1m"
END = "\033[0m"

SOLVED = [
     [5, 1, 7, 3, 4, 9, 8, 6, 2],
     [6, 4, 2, 7, 8, 1, 5, 9, 3],
     [8, 9, 3, 6, 2, 5, 1, 4, 7],
     [7, 6, 4, 9, 5, 1, 2, 3, 8],
     [2, 1, 8, 4, 6, 3, 5, 9, 7],
     [9, 3, 5, 7, 2, 8, 4, 1, 6],
     [1, 2, 5, 3, 7, 9, 4, 8, 6],
     [8, 3, 4, 1, 5, 6, 9, 7, 2],
     [6, 7, 9, 2, 8, 4, 3, 5, 1],
]

BOARD = [[0, 0, 0, 3, 0, 0, 0, 6, 0],
         [0, 0, 0, 0, 8, 0, 0, 0, 3],
         [0, 9, 0, 0, 2, 0, 1, 0, 0],
         [0, 0, 0, 2, 1, 0, 0, 0, 0],
         [9, 0, 1, 4, 0, 0, 0, 2, 8],
         [0, 0, 0, 0, 0, 7, 0, 0, 6],
         [0, 0, 0, 0, 3, 4, 0, 0, 0],
         [0, 7, 0, 0, 0, 6, 2, 8, 0],
         [4, 0, 6, 9, 0, 0, 0, 5, 0],]

# SOLVED = [[3, 1, 6, 5, 7, 8, 4, 9, 2],
#           [5, 2, 9, 1, 3, 4, 7, 6, 8],
#           [4, 8, 7, 6, 2, 9, 5, 3, 1],
#           [2, 6, 3, 4, 1, 5, 9, 8, 7],
#           [9, 7, 4, 8, 6, 3, 1, 2, 5],
#           [8, 5, 1, 7, 9, 2, 6, 4, 3],
#           [1, 3, 8, 9, 4, 7, 2, 5, 6],
#           [6, 9, 2, 3, 5, 1, 8, 7, 4],
#           [7, 4, 5, 2, 8, 6, 3, 1, 9],]

# BOARD = [[3, 0, 6, 5, 0, 8, 4, 0, 0], 
#          [5, 2, 0, 0, 0, 0, 0, 0, 0], 
#          [0, 8, 7, 0, 0, 0, 0, 3, 1], 
#          [0, 0, 3, 0, 1, 0, 0, 8, 0], 
#          [9, 0, 0, 8, 6, 3, 0, 0, 5], 
#          [0, 5, 0, 0, 9, 0, 6, 0, 0], 
#          [1, 3, 0, 0, 0, 0, 2, 5, 0], 
#          [0, 0, 0, 0, 0, 0, 0, 7, 4], 
#          [0, 0, 5, 2, 0, 6, 3, 0, 0],]


def bolded(text: str):
    return BOLD + text + END


# def display(board):
#     """
#     Function to display the required board when needed
#     """
#     i = 0
#     while i < 9:
#         for x, y, z in zip(board[i],
#          board[i+1],
#          board[i+2]):
#             print(end=" ")
#             print(*x, end=bolded(" | "))
#             print(*y, end=bolded(" | "))
#             print(*z,)

#         i += 3
#         if i < 9:
#             print(bolded("\u2500" * 7), bolded("\u2500" * 7), bolded("\u2500" * 7))


def display(npboard):
    i = 0
    while i < 9:
        row = npboard[i]
        print(end=" ")
        
        for j in range(0, 9, 3):
            print(*row[j:j+3], end="")
            if j < 6:
                print(end=bolded(" | "))
            else:
                print(end="\n")
        
        i += 1
        if i % 3 == 0 and i < 9:
            print(bolded("\u2500" * 7), bolded("\u2500" * 7), bolded("\u2500" * 7))
            
    print()
        # print()
        # print(row[:3], row[3:6], row[6:9], sep=bolded(" | "))


def displayed(function):
    """
    Decorator that displays the board after executing the function call
    """

    def wrapper(board=None, *args, **kwargs):
        return_val = function(*args, **kwargs)
        if board is not None:
            display(board)

        return return_val

    return wrapper
# displayed(main)()

@displayed
def test_check():
    print(all(0 not in line for line in SOLVED))
    print(all(0 not in line for line in BOARD))


if __name__ == '__main__':
    test_check()