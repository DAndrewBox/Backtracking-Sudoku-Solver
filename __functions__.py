from os import system
from __sudoku__ import SUDOKU


def get_next_empty_cell(grid: list) -> bool:
    """ Get the next cell that's available to change """
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            is_empty: bool = (grid[row][col] == '.')
            if is_empty:
                cell_info = {"can_change": is_empty,
                            "col": col,
                            "row": row
                            }
                return cell_info
    
    return {"can_change": False}


def get_row_avaliable(grid: list, value: str, row: int) -> bool:
    """ Check if can put this number on this row. """
    for i in range(9):
        if grid[row][i] == value:
            return False

    return True


def get_col_avaliable(grid: list, value: str, col: int) -> bool:
    """ Check if can put this number on this col. """
    for i in range(9):
        if grid[i][col] == value:
            return False

    return True


def get_block_avaliable(grid: list, value: str, row: int, col: int) -> bool:
    """ Check if can put this number based on the sudoku block. """
    xblock: int = int(col / 3) * 3
    yblock: int = int(row / 3) * 3

    for i in range(yblock, yblock + 3):
        for j in range(xblock, xblock + 3):
            if grid[i][j] == value:
                return False

    return True


def sudoku_solver(sudoku: list, show_steps: bool = False) -> bool:
    """ Solve the Sudoku using backtracking. """
    row: int = 0
    col: int = 0
    cell: dict = get_next_empty_cell(sudoku)

    if (cell['can_change'] == False):
        return True

    row, col = (cell['row'], cell['col'])

    for i in range(1, 10):
        value = str(i)
        can_put_number: bool = (get_row_avaliable(sudoku, value, row) and
                                get_col_avaliable(sudoku, value, col) and
                                get_block_avaliable(sudoku, value, row, col)
                                )

        if (can_put_number):
            sudoku[row][col] = value
            if (sudoku_solver(sudoku, show_steps)):
                return True

            sudoku[row][col] = '.'

    return False


def show(grid):
    """ Show the Grid """
    for i in range(9):
        if i == 3 or i == 6:
            print('-------------------------')
        for j in range(9):
            if j == 3 or j == 6:
                print(' | ', end=' ')
            if j < 8:
                print(grid[i][j], end=' ')
            else:
                print(grid[i][j], end='\n')

sudoku_solver(SUDOKU)
show(SUDOKU)
