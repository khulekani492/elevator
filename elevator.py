

def blank_space(board):
    """Find an empty space on the board."""
    for row in range(9):
        for cell in range(9):
            if board[row][cell] == 0:
                return row, cell
    return None, None


def valid_n(board,  row, cell):
    """Check if the guess is valid for the given cell."""
    numbers = [1,2,3,4,5,6,7,8,9]
    candidates = board[row][cell] = set()

    rw = []
    
    # Check the column
    cell_values = [board[i][cell] for i in range(9)]
    
    for n in numbers:
         if n not in cell_values and n not in board[row]:
             candidates.add(n)
    

    # Check the 3x3 grid
    subgrid = []
    row_start = (row // 3) * 3
    cell_start = (cell // 3) * 3    
    for r in range(row_start, row_start + 3):
        for c in range(cell_start, cell_start + 3):
            for n in numbers:
               if n not in cell_values and n not in board[row] and n != board[r][c]:
                   
                   candidates.add(n)
                    
    return candidates
steps = []
#going through the indexed position and looking for singles and removing them for duplicate 
def elimination(board):
    for item in board:
        if isinstance(item,set):
            
            pass 

def solve_sudoku(board):
    """Solve the Sudoku puzzle using backtracking."""
       
    row, cell = blank_space(board)
    # If no empty space, the board is solved
    if row is None:
        return True

    # Try all numbers from 1 to 9
    
    board[row][cell] = valid_n(board,row,cell)
            # Recursively try to solve the board
    if len(board[row][cell]) == 1:
        convert_to_list = list(board[row][cell]) 
        r = board[row]
        board[row][cell] = convert_to_list[0] 
    #     if board[row] == 8:
    #         if board[cell] > 4:
    #             print(f"Naked Single: Top right cell can only be a {board[row][cell]}")
    # elif len(board[row][cell]) == 2:
    #     convert_to_list = list(board[row][cell]) 
    #     board[row][cell] = convert_to_list[0]
    #     if board[row] == 8:
    #         if board[cell] > 4:
    #             print(f"Naked Single: Top right cell can only be a {board[row][cell]}")
    # elif len(board[row][cell]) == 3:
    #     convert_to_list = list(board[row][cell]) 
    #     board[row][cell] = convert_to_list[0]
    #     if board[row] == 8:
    #         if board[cell] > 4:
    #             print(f"Naked Single: Top right cell can only be a {board[row][cell]}")

    # elif len(board[row][cell]) == 4:
    #     convert_to_list = list(board[row][cell]) 
    #     board[row][cell] = convert_to_list[0]
    #     if board[row] == 8:
    #         if board[cell] > 4:
    #             print(f"Naked Single: Top right cell can only be a {board[row][cell]}")


    for i in range(1):
        solve_sudoku(board)
        
    return board
            # Backtrack
    # If no valid number works, return False.py
    return False

def print_board(board):
    """Print the Sudoku board in a readable format."""
    for row in board:
        print(" ".join(str(num) for num in row))

# Input Sudoku board
board = [
    [9, 6, 2, 0, 7, 8, 5, 0, 0],
    [1, 0, 5, 0, 0, 9, 3, 0, 0],
    [3, 0, 0, 0, 0, 0, 8, 2, 0],
    [0, 0, 1, 0, 0, 0, 0, 7, 0],
    [6, 0, 0, 0, 5, 0, 0, 0, 8],
    [0, 0, 0, 6, 0, 3, 9, 0, 5],
    [0, 1, 8, 0, 0, 5, 0, 0, 0],
    [0, 0, 6, 8, 3, 2, 7, 0, 1],
    [7, 5, 3, 1, 9, 0, 4, 8, 0]
]

# [9 6 2 3 7 8 5 1 4
# 1 8 5 4 2 9 3 6 7
# 3 7 4 5 6 1 8 2 9
# 5 3 1 9 8 4 2 7 6
# 6 4 9 2 5 7 1 3 8
# 8 2 7 6 1 3 9 4 5
# 2 1 8 7 4 5 6 9 3
# 4 9 6 8 3 2 7 5 1
# 7 5 3 1 9 6 4 8 2 ]
# Solve the Sudoku puzzle


def main():
    """Main function to read input, solve the puzzle, and write output."""
    # Get command-line arguments
    

    # Read the board from the input file
    # try:
    #     with open('puzzle.txt', "r") as file:
    #         lines = file.readlines()
    #     board = [[int(num) for num in line.strip().split()] for line in lines]
    # except Exception as e:
    #     print(f"Error reading input file: {e}")
    #     return

    # Ensure the board is valid
    # Solve the puzzle
main()


print(solve_sudoku(board))


if len(board) != 9 or not all(len(row) == 9 for row in board):
    print("Invalid board format. Ensure the board is a 9x9 grid.")
        



