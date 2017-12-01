from random import randint
board = [["O"]*5 for _ in range 5]

def print_board:
    for row in board:
        print(" ".join(row))

col = randint(0, len(board[0]))
row = randint(0, len(board))

print(row, col)

row_guess = input("Guess row: ")
col_guess = input("Guess column: ")

if row_guess == row and col_guess == col:
    print("something like \"We have a winner\"")
