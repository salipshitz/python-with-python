from random import randint
board = [["O"]*5 for _ in range 5]

def print_board():
    for row in board:
        print(" ".join(row))

col = randint(0, len(board[0]))
row = randint(0, len(board))

print(row, col)

row_guess = input("Guess row: ") - 1
col_guess = input("Guess column: ") - 1

print_board()
if row_guess == row and col_guess == col:
    print("something like \"We have a winner\"")
elif row_guess > len(board) or col_guess > len(board[0]) or row_guess < 0 or col_guess < 0:
    print("Next time, try to aim *inside* the ocean")
elif board[row_guess][col_guess] == 'x':
    print("Insanity: doing the same thing over and over again and expecting different results.")
else:
    board[row_guess][col_guess] = 'x'
    print("YOU SAX!!!")
