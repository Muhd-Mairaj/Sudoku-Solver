from Resources.resources import SOLVED, TEST_SUBPARTS, TEST_ROW, TEST_COL
from main import get_subpart_index, get_subpart, get_row_col
from random import randint


def test_get_subpart_index():
    print("RUNNING: test_get_subpart_index")
    works = True

    i, j, expected = 1, 4, 1 
    if get_subpart_index(i, j) != expected:
        works = False
        print(f"row_col_getter({i}, {j}) expected: {expected}; got {get_subpart_index(i, j)}")

    i, j, expected = 1, 7, 2 
    if get_subpart_index(i, j) != expected:
        works = False
        print(f"row_col_getter({i}, {j}) expected: {expected}; got {get_subpart_index(i, j)}")

    i, j, expected = 5, 7, 5 
    if get_subpart_index(i, j) != expected:
        works = False
        print(f"row_col_getter({i}, {j}) expected: {expected}; got {get_subpart_index(i, j)}")
    
    if works:
        print("SUCCESS")
    print()


def test_get_subparts():
    print("RUNNING: test_get_subparts")

    works = True
    for _ in range(10):
        i, j = randint(0, 8), randint(0, 8)
        expected = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        if get_subpart(TEST_SUBPARTS, i, j) != expected:
            works = False
            print(f"get_subpart(TEST_SUBPARTS, {i}, {j}) expected: {expected}; got", get_subpart(TEST_SUBPARTS, i, j))

    # i, j = randint(0, 8), randint(0, 8)
    # printf("Check this one yourself")
    # print(f"get_subpart(SOLVED, {i}, {j}) gave:", get_subpart(SOLVED, i, j))

    if works:
        print("SUCCESS")
    print()


def test_get_row_and_col():
    print("RUNNING: test_get_row_and_col")

    works = True

    # USING TEST_ROW and TEST_COL
    for _ in range(10):
        row, col = randint(0,8), randint(0,8)
        expected_row = [9 * row + i for i in range(1,10)]
        expected_col = [9 * col + i for i in range(1,10)]

        if get_row_col(TEST_ROW, row, col)[0] != expected_row:
            works = False
            print(f"get_row_col(TEST_ROW, {row}, {col})[0] expected: {expected_row}; got {get_row_col(TEST_ROW, row, col)[0]}")

        if get_row_col(TEST_COL, row, col)[1] != expected_col:
            works = False
            print(f"get_row_col(TEST_COL, {row}, {col})[1] expected: {expected_col}; got {get_row_col(TEST_COL, row, col)[1]}")
    

    if works:
        print("SUCCESS")
    print()



if __name__ == "__main__":
    test_get_subpart_index()
    test_get_subparts()
    test_get_row_and_col()