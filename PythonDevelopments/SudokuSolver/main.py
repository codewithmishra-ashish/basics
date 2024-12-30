def print_board(board):
    """Prints the Sudoku board."""
    for row in board:
        print(" ".join(str(num) if num != 0 else '.' for num in row))

def is_valid(board, row, col, num):

    # Check the row
    if num in board[row]:
        return False
    
    # Check the column
    for r in range(9):
        if board[r][col] == num:
            return False
    
    # Check the 3x3 grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if board[r][c] == num:
                return False
    
    return True

def find_empty_location(board):
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                return (r, c)
    return None

def sudoku_solver(board):
    empty_location = find_empty_location(board)
    
    if not empty_location:
        return True  
    
    row, col = empty_location
    
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            
            if sudoku_solver(board):
                return True
            
            board[row][col] = 0  
    
    return False

# Example Sudoku board (0s are placeholders for empty cells)
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if sudoku_solver(sudoku_board):
    print("Sudoku solved successfully:")
    print_board(sudoku_board)
else:
    print("No solution exists.")
