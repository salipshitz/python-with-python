from random import randint
enem_board = [[u"\U0001F30A"]*5 for n in range(5)]
frnd_board = [[u"\U0001F30A"]*5 for n in range(5)]
name = "Sa'ar"
def print_board(frnd, enem):
    print("CPU")
    print(end="  ")
    for i in range(1, len(enem[0])+1):
        print(i, end="  ")
    print()
    for i in range(1, len(enem[0])+1):
        row = enem[i-1]
        print(i," ".join(row))
    print("-".join(["--"]*5))
    print(name)
    print(end="  ")
    for i in range(1, len(frnd[0])+1):
        print(i, end="  ")
    print()
    for i in range(1, len(frnd)+1):
        row = frnd[i-1]
        print(i," ".join(row))
    print()
#computer hide
row = randint(0, len(enem_board)-1)
col = randint(0, len(enem_board[0])-1)
#player hide
pr = None
pc = None
while pr == None and pc == None:
    if pr == None:
        pr = randint(1, len(frnd_board))
        pr -= 1
    if pc == None:
        pc = randint(1, len(frnd_board))
        pc -= 1
    if pc < 0 or pc >= len(frnd_board[0]):
        pc = None
    if pr < 0 or pr > len(frnd_board):
        pr = None
else:
    print(pr+1,pc+1)
    frnd_board[pr][pc] = u"\U0001F6A2"
    
won = False
lost = False
while (not won) and (not lost):
    print_board(frnd_board, enem_board)
    print("CPU: ")
    t = False
    while not t:
        gr = randint(0, len(frnd_board)-1)
        gc = randint(0, len(frnd_board[0])-1)
        if frnd_board[gr][gc] != u"\U0001F4A3":
            t = True
    print("Row: ",gr+1)
    print("Column: ",gc+1)
    print()
    if frnd_board[gr][gc] == u"\U0001F6A2":
        lost = True
        frnd_board[gr][gc] = u"\U0001F4A5"
        print("Hit!")
        break
    else:
        frnd_board[gr][gc] = u"\U0001F4A3"
        print("Miss!")
    print()
    print_board(frnd_board, enem_board)
    print(name+":")
    gr = randint(1, len(enem_board))
    gr -= 1
    print("Row:",gr)
    gc = randint(1, len(enem_board[0]))
    gc -= 1
    print("Column:",gc)
    print()
    if gr == row and gc == col:
        print("Hit!")
        enem_board[gr][gc] = u"\U0001F4A5"
        won = True
    elif gr < 0 or gr >= len(enem_board) or gc < 0 or gc >= len(enem_board[0]):
        print("That's not even in the ocean ):")
    elif enem_board[gr][gc] == u"\U0001F4A3":
        print("You already guessed that, stupid! DX")
    else:
        print("Miss!")
    print()
    enem_board[gr][gc] = u"\U0001F4A3"
if won:
    for i in range(len(enem_board)):
        for j in range(len(enem_board[i])):
            if not enem_board[i][j] == u"\U0001F4A3":
                enem_board[i][j] = u"\U0001F525"
            else:
                enem_board[i][j] = u"\u2620"
    enem_board[row][col] = u"\U0001F4A5"
    print("Congrats on winning!")
if lost:
    for i in range(len(frnd_board)):
        for j in range(len(frnd_board[i])):
            if not frnd_board[i][j] == u"\U0001F4A3":
                frnd_board[i][j] = u"\U0001F525"
            else:
                frnd_board[i][j] = u"\u2620"
    frnd_board[pr][pc] = u"\U0001F4A5"
    enem_board[row][col] = u"\U0001F6A2"
    print("You sax. Better luck next time!")
print_board(frnd_board, enem_board)
