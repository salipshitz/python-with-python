from random import randint

width = 5
height = 20
board = [["O"]*height]*width

def print_board(board):
    for row in board:
        for char in row:
            print(char, end=" ")
        print()

row = randint(0, len(board)-1)
col = randint(0, len(board[0])-1)

board[row][col] = "X"

print_board(board)
