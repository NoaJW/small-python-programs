# Qns: https://inventwithpython.com/bigbookpython/project73.html

# TODO: Choose move to undo, not just last move

import requests, random, sys

def isValueAllowed(matrix, row_idx, col_idx, row, col, val):    
    if matrix[row_idx][col_idx] != 0:
        print("Cell is already filled")
        return False
    
    if val in row:
        print("Digit is already in the row")
        return False
    
    if val in col:
        print("Digit is already in the col")
        return False
    
    # Check if square (9 cells) has the digit     
    row_to_check = []
    col_to_check = []
    row_to_check.extend(getNeighbours(row_idx))
    col_to_check.extend(getNeighbours(col_idx))

    for i in row_to_check:
        for j in col_to_check:
            if i == row_idx and j == col_idx:       # Skip the current cell
                continue
            if matrix[i][j] == val:
                print("Digit is already in the square")
                return False
  
    return True


def getNeighbours(idx):
    if (idx + 1) % 3 == 0:              # last index in pair of 3 
        return idx - 2, idx - 1, idx
    if (idx + 1) % 3 == 2:              # middle index in pair of 3 
        return idx - 1, idx, idx + 1
    if (idx + 1) % 3 == 1:              # first index in pair of 3 
        return idx, idx + 1, idx + 2


def checkSolved(matrix): 
    return any(0 in row for row in matrix)


def displayGrid(matrix):
    grid = "  A B C   D E F   G H I\n"

    for i in range(9):
        if i % 3 == 0 and i != 0:
            grid += "  ------+-------+------\n"
        grid += f"{i + 1} "
        for j in range(9):
            if j % 3 == 0 and j != 0:
                grid += "| "
            grid += f"{matrix[i][j] if matrix[i][j] != 0 else '.'} "
        grid += "\n"

    print(grid)


def getPuzzles():
    url = "https://inventwithpython.com/sudokupuzzles.txt"

    try:
        response = requests.get(url)
        response.raise_for_status()         # Check for any errors in the response
        return response.text.splitlines()      
    except requests.RequestException as e:
        print(f"Error downloading the text file: {e}")


def getRandomPuzzle(puzzles):
    return random.choice(puzzles)           
   

def setPuzzle(puzzle, matrix):
    for i in range(81):                      # 81 characters in the puzzle string
        row = i // 9
        col = i % 9

        if puzzle[i].isdecimal(): 
            matrix[row][col] = int(puzzle[i])
        else:
            matrix[row][col] = 0

    return matrix


def main(): 
    matrix = [[0 for _ in range(9)] for _ in range(9)]      
    alphabet_mapping = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8}
    other_options = ["RESET", "NEW", "UNDO", "QUIT"]
    puzzles = getPuzzles()
    moves = []
    
    # Get a random puzzle and set it in the matrix 
    puzzle = getRandomPuzzle(puzzles)       # Original puzzle
    matrix = setPuzzle(puzzle, matrix)
    print("= Original puzzle =\n")
    displayGrid(matrix)

    print("""
Enter a move, or RESET, NEW, UNDO, or QUIT:
(For example, a move looks like "B4 9".)""")
    
    # Infinite loop for move, until QUIT or keyboard interrupt error is inputted 
    while True:

        # Input move and validation
        while True: 
            try: 
                move = input("> ")
            except KeyboardInterrupt:
                print("KeyboardInterrupt received. Exiting program...")
                sys.exit()

            if move.upper() in other_options:
                break
            else: 
                # Validate move input
                if len(move) != 4:
                    print("For move: Please input only 4 characters.")
                    continue
                if move[0].upper() not in alphabet_mapping: 
                    print("For move: First character has to be an alphabet from A to I")
                    continue
                if not move[1].isdecimal() or move[1] == '0':
                    print("For move: Second character has to be a digit from 0 to 9 (e.g. 4 in B4)")
                    continue
                if not move[3].isdecimal() or move[3] == '0':
                    print("For move: Last character has to be a digit from 0 to 9 (e.g. 9 in B4 9)")
                    continue
                break

        # Other move options
        if move.upper() == "QUIT": 
            print("Thanks for playing!")
            break
        
        if move.upper() == "RESET":
            matrix = setPuzzle(puzzle, matrix)
            moves = []
            print("= Resetted to original puzzle =\n")
            displayGrid(matrix)
            continue

        if move.upper() == "NEW":
            puzzle = getRandomPuzzle(puzzles)  
            matrix = setPuzzle(puzzle, matrix)
            moves = []
            print("= New puzzle =\n")
            displayGrid(matrix)
            continue

        if move.upper() == "UNDO":
            if len(moves) > 0: 
                last_move = moves.pop()                 # [row_idx, col_idx, val]
                matrix[last_move[0]][last_move[1]] = 0
                print("= Undo move =\n")
                displayGrid(matrix)
                continue
            else:
                print("No move to undo!")
                continue
        
        # Move 
        row_idx = int(move[1]) - 1
        col_idx= alphabet_mapping[move[0].upper()] 
        val = int(move[3])

        col = []
        for i in range(9):
            col.append(matrix[i][col_idx])      

        # Check if move is allowed 
        if not isValueAllowed(matrix, row_idx, col_idx, matrix[row_idx], col, val):
            continue

        # Add move to moves list 
        moves.append([row_idx, col_idx, val])
        
        # Update matrix 
        matrix[row_idx][col_idx] = val
        displayGrid(matrix)
            
        # Check if puzzle solved
        if not checkSolved(matrix):
            print("You win!")
            print("Thanks for playing!")
            break


if __name__ == '__main__':
    main()

