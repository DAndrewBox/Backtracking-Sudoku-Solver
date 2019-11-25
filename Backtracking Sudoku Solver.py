'''
Backtracking Sudoku Solver
D' Andrëw Box
2018-11-04
'''

import os;

# Check 0's
def can_put_number(grid):
    for i in range(0, 9):
        for j in range (0, 9):
            if grid[i][j] == '.':
                _cell_info = {'row': i,
                              'col': j,
                              'can_put': True};
                return _cell_info;

    _cell_info = {'row': None,
                  'col': None,
                  'can_put': False};
    return _cell_info;

# Check if can put a number as "num" checking Sudoku official rules
def check_space(grid, num, _row, _col):
    # Check row
    for i in range(0, 9):
        if grid[_row][i] == str(num):
            #print('WRONG BY ROWS');
            return False;
        
    # Check column
    for i in range(0,9):
        if grid[i][_col] == str(num):
            #print('WRONG BY COLUMNS');
            return False;

    # Check blocks
    _xblock, _yblock  = (int(_col/3), int(_row/3));
    for i in range(_yblock*3, _yblock*3+3):
        for j in range(_xblock*3, _xblock*3+3):
            if grid[i][j] == str(num):
                #print('WRONG BY BLOCK');
                return False;
            
    return True;

# Solver
def solve(grid, step_by_step):
    _row, _col = (0, 0);

    _cell = can_put_number(grid);
    if _cell['can_put'] == False:
        return True;
    
    _row, _col = (_cell['row'], _cell['col']);

    for i in range(1, 10):
        if check_space(grid, i, _row, _col):
            grid[_row][_col] = str(i);
            if (step_by_step == "Y"):
                if _col == 8:
                    show(grid);
                    os.system('cls');
            
            if solve(grid, step_by_step) == True:
                return True;

            grid[_row][_col] = '.';
    return False;

# Show grid
def show(grid):
    for i in range(9):
        if i==3 or i==6:
            print('-------------------------');
        for j in range(9):
            if j==3 or j==6:
                print(' | ', end=' ');
            if j < 8:
                print(grid[i][j], end=' ');
            else:
                print(grid[i][j], end='\n');
    print('');

#########################################################
# This sudoku is the World's Hardest Sudoku

sudoku = [['8','.','.', '.','.','.', '.','.','.'],
          ['.','.','3', '6','.','.', '.','.','.'],
          ['.','7','.', '.','9','.', '2','.','.'],
          
          ['.','5','.', '.','.','7', '.','.','.'],
          ['.','.','.', '.','4','5', '7','.','.'],
          ['.','.','.', '1','.','.', '.','3','.'],

          ['.','.','1', '.','.','.', '.','6','8'],
          ['.','.','8', '5','.','.', '.','1','.'],
          ['.','9','.', '.','.','.', '4','.','.']];

show_steps = "";

print("SUDOKU TO SOLVE: \n");
show(sudoku);

while (show_steps != "Y" and show_steps != "N"):
    show_steps = input("Wanna see step by step? [Y/N]: ");
    show_steps = show_steps.upper();

solve(sudoku, show_steps);
os.system('cls');

print("SUDOKU SOLVED: \n")
show(sudoku);
input('Press any key to close...');
