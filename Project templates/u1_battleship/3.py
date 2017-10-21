width = 5
height = 5
board = [["O"]*height]*width

def print_board(board):
    for row in board:
        print(" ".join(row))
    

print_board(board)
