board = [
    [" ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " "]
]

first_marker = "X" #determines the marker for player 1
second_marker = "O" #determines the marker for player 2
win = False #win/loss variable - if its true, the game should stop
current_player = "Player One" #determines who needs to play

# This function prints the board.
def print_board():
    print(" 1 2 3 4 5 6 7")
    for i in range(len(board)):
        for j in board[i]:
            print(j+"|",end="")
        print("")

print_board()

def player_one():
    global board
    marker = "X"
    ask = int(input("What column would you like to play? "))
    if board[0][ask] != " ":
        print("Play another column")
        player_one()
    for i in range(6, -1, -1):
        if board[i][ask] != " ":
            continue
        else:
            board[i][ask] = marker
            break
    print_board()
    win_loss()
    if not win: #checks if the other player won or nah
        player_two()#if not return to other player by calling that function 

def player_two():
    global board
    marker = "O"
    ask = int(input("What column would you like to play? "))
    if board[0][ask] != " ":
        print("Play another column")
        player_two()  
    for i in range(6, -1, -1):
        if board[i][ask] != " ":
            continue
        else:
            board[i][ask] = marker
            break
    print_board()
    win_loss()
    if not win:  
        player_one()

def win_loss():
    global win
    #allows me to edit win bcuz without it it is out of range
    # checks a horizontal win
    for row in range(len(board)):#checks only the length of the board
        for col in range(len(board[0]) - 3):#checks every row but stops at fourth to last row using -3 so we dont go outta range checking
            if board[row][col] == board[row][col + 1] == board[row][col + 2] == board[row][col + 3] != " ":#checks if next 3 rows are also filled by checking if theyre equal, and if they have "" then it cant be equal  
                print(f"{current_player} wins by hori")
                win = True #changes value of win variable which is why we used global earlierr 
                return
    
    # checks for vertical win
    # pretty much method as hort but switches up the col and row placement 
    for col in range(len(board[0])):
        for row in range(len(board) - 3):
            if board[row][col] == board[row + 1][col] == board[row + 2][col] == board[row + 3][col] != " ":
                print(f"{current_player} wins by vert")
                win = True
                return

# This runs the game... be careful running this (infinite loop)
while not win:
    if current_player == "Player One":
        player_one()
    if current_player == "Player Two":
        player_two()
