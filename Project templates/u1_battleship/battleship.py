from random import randint
board = []
board = [["O"]*5 for i in range(5)]
def print_board(board):
    for row in board:
        print(" ".join(row))
print_board(board)
row = randint(0, len(board)-1)
col = randint(0, len(board[0])-1)
print(row, col)
guesses = 3
while guesses > 0:
    print(guesses,"guesses left")
    gr = int(input("Guess row: "))-1
    gc = int(input("Guess col: "))-1
    if gr == row and gc == col:
        print("Congrats on winning.")
        board[row][col] = "C"
        break
    elif gr >= len(board) or gc >= len(board[0]):
        print("That's not even in the ocean. Try again.")
        continue
    elif board[gr][gc] == "X":
        print("You already guessed that. Trying.")
        continue
    else:
        print("You sax.")
        board[gr][gc] = "X"
    print_board(board)
    guesses -= 1
