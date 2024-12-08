#Project a simply elevator
#Aim manipulating strings based on the user input
#Author Khulekani Zondo DAte :02 May 2022



# with open('puzzle.txt','r') as file:

#     thefile = file.readlines()

# valid_num = ['1','2','3','4','5','6','7','8','9']
# lines_from_file = []
# to_list = []
# horizotal= []
# straight = [] 

# for i in thefile:
#     lines_from_file.append(i.replace('\n','').replace(' ',''))


# for line in lines_from_file:
    
#     to_list.append(list(line))

# # Convert each string to an integer
# int_board = [[int(num) for num in row] for row in to_list]
# baord = int_board

# #print(to_list)
# # for line in to_list:
# #     print(line)
# # print("_______________________________________")

# #                 # for x in range(2):
# #                 #      current.append(to_list[line][i + x])
# #                 # find_sub_first_row.append(current)
                
        
# # # print(find_sub_first_ro

# # def sub(board=to_list):

# #     coord = [(0,0), (0, 3), (0, 6),
# #              (3, 0), (3, 3), (3, 6),
# #              (6, 0), (6, 3), (6, 6)]
    
# #     results = []

# #     for row, col in coord:
# #         sub_grid = []

# #         for i in range(3):
# #             roww = []
# #             for j in range(3):
# #                 roww.append(board[row + i][col + j])
# #             sub_grid.append(roww)
# #         results.append(sub_grid)

# #     return results 

# # print(sub())
# # available = []
# # for s in sub():
# #     for row in range(3):
# #         print(s[row]) 
# #         current = s[row]
# #         for n in valid_num:
# #             if n in current:
# #                 available.append(n)
# #         for x in available:
# #             if x in to_list:
# #                 print(row)
                
   
# #         for indexes in range(len(current)):
# #             if current[indexes] == '0':
# #                 print(indexes) #take the index go to your board and return the table going down 
                 
                        
# #     break
# # possible_play = []    
# # #print(available)
# # for n in valid_num:
# #     if n not in available:
# #         possible_play.append(n)

# # print(possible_play,' possible moves')
# # # let take possible moves 
# # # check the row of each nested list 


# with open('puzzle.txt','r') as file:

#     thefile = file.readlines()

# valid_num = ['1','2','3','4','5','6','7','8','9']
# lines_from_file = []
# to_list = []
# horizotal= []
# straight = [] 

# for i in thefile:
#     lines_from_file.append(i.replace('\n','').replace(' ',''))


# for line in lines_from_file:
    
#     to_list.append(list(line))

# # Convert each string to an integer
# int_board = [[int(num) for num in row] for row in to_list]
# baord = int_board

# def blank_space(board):
#     #finding an empty space and return it index row,cell the row being the nested list the cell being the position inside the nested list
#     for row in range(9):
#         for cell in range(9):
#             if board[row][cell] == 0 :
#                 return row,cell
#     return None ,None

# def valid_n(board,guess,row,cell):
#     row_values = board[row]
#     if guess in row_values:
#         return False
#     # cells_values = []
    
#     # for i in range(9):
#     #     cells_values(board[i][cell])
#     cell_values = [board[i][cell] for i in range(9)]
#     if guess in cell_values:
#         return False
#     row_start = (row // 3) * 3
#     cell_start = (cell // 3) * 3
#     for r in range(row_start, row_start + 3):
#        for c in range(cell_start, cell_start + 3):
#           if board[r][c] == guess:
#             return False
#     return True

# def solve_suduko(board):
#     row,cell = blank_space(board)
 
#     if row is None:
#         return True
#     # a guess from 1 , 9
#     for guess in range(1,10):
#         if valid_n(board,guess,row,cell):
#             board[row][cell] = guess
            
#             # call the function 
#             if solve_suduko(board):
#                 return True
#     #backtracking  replacing the number back to zero
#         board[row][cell] = 0 

#     #if no solution found
#         return False
# solve_suduko(int_board)
# # how to return the solved board on your terminal
# def print_board(board):
#     """Print the Sudoku board in a readable format."""
#     for row in board:
#         print(" ".join(str(num) for num in row))

# # Solve the Sudoku puzzle
# if solve_suduko(int_board):
#     print("Solved Sudoku Board:")
#     print_board(int_board)
# else:
#     print("No solution exists for the given Sudoku puzzle.")

import sys 

def blank_space(board):
    """Find an empty space on the board."""
    for row in range(9):
        for cell in range(9):
            if board[row][cell] == 0:
                return row, cell
    return None, None


def valid_n(board, guess, row, cell):
    """Check if the guess is valid for the given cell."""
    # Check the row
    if guess in board[row]:
        return False

    # Check the column
    cell_values = [board[i][cell] for i in range(9)]
    if guess in cell_values:
        return False

    # Check the 3x3 grid
    row_start = (row // 3) * 3
    cell_start = (cell // 3) * 3
    for r in range(row_start, row_start + 3):
        for c in range(cell_start, cell_start + 3):
            if board[r][c] == guess:
                return False

    return True
steps = []

def solve_sudoku(board):
    """Solve the Sudoku puzzle using backtracking."""
       
    row, cell = blank_space(board)

    # If no empty space, the board is solved
    if row is None:
        return True

    # Try all numbers from 1 to 9
    for guess in range(1, 10):
        if valid_n(board, guess, row, cell):
            board[row][cell] = guess
            steps.append(f"Trying {guess} at ({row}, {cell})")
            # Recursively try to solve the board
            if solve_sudoku(board):
                return True

            # Backtrack
            print(f"Backtracking at ({row}, {cell})")
            board[row][cell] = 0

    # If no valid number works, return False
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

# Solve the Sudoku puzzle
if solve_sudoku(board):
    print("Solved Sudoku Board:")
    print_board(board)
else:
    print("No solution exists for the given Sudoku puzzle.")

def main():
    """Main function to read input, solve the puzzle, and write output."""
    # Get command-line arguments
    if len(sys.argv) != 4:
        print("Usage: python solve.py path/to/puzzle.txt -o path/to/solved_puzzle.txt")
        return

    input_file = sys.argv[1]
    output_flag = sys.argv[2]
    output_file = sys.argv[3]

    if output_flag != "-o":
        print("Invalid flag. Use -o to specify the output file.")
        return

    # Read the board from the input file
    try:
        with open(input_file, "r") as file:
            lines = file.readlines()
        board = [[int(num) for num in line.strip().split()] for line in lines]
    except Exception as e:
        print(f"Error reading input file: {e}")
        return

    # Ensure the board is valid
    if len(board) != 9 or not all(len(row) == 9 for row in board):
        print("Invalid board format. Ensure the board is a 9x9 grid.")
        return

    # Solve the puzzle
    
    if solve_sudoku(board, steps):
        result = "Solved Sudoku Board:\n" + print_board(board)
    else:
        result = "No solution exists for the given Sudoku puzzle."

    # Write the result and steps to the output file
    try:
        with open(output_file, "w") as file:
            file.write("\n".join(steps) + "\n\n" + result)
        print(f"Steps and solved board written to {output_file}")
    except Exception as e:
        print(f"Error writing to output file: {e}")


if __name__ == "__main__":
    main()





