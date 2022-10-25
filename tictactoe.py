board = [ 
    [' _ ', ' _ ', ' _ '],

    [' _ ', ' _ ', ' _ '],
    
    [' _ ', ' _ ', ' _ ']
]
current_player = ' X '
GameRun = True
var = False
row = 0
col = 0

def Print_board(board): # Creates the Board for TicTacToe

    print(f"| {board[0][0]} | {board[0][1]} | {board[0][2]} |")
    print("-------------------")
    print(f"| {board[1][0]} | {board[1][1]} | {board[1][2]} |")
    print("-------------------")
    print(f"| {board[2][0]} | {board[2][1]} | {board[2][2]} |")
    print("-------------------")

def playerInput(board, current_player): # Takes Input from the user

    global player
    player = int(input("Enter the number from 1-9: "))
    global row
    row = (player - 1)//3
    global col
    col = (player - 1) %3
    if board[row][col] == ' _ ':
        board[row][col] = current_player
    else:
        print("That slot is occupied")
    
def WinLogic(board, row, col, current_player): # Decides who won the game

        if board[row][0] == board[row][1] == board[row][2]:
            Print_board(board)
            print(f"{current_player} wins! GG!")
            return True
        if board[0][col] == board[1][col] == board[2][col]:
            Print_board(board)
            print(f"{current_player} wins! GG!")
            return True
        if board[0][0] == board[1][1] == board[2][2] == (' X ' or ' O '):
            Print_board(board)
            print(f"{current_player} wins! GG!")
            return True
        if board[0][2] == board[1][1] == board[2][0] == (' X ' or ' O '):
            Print_board(board)
            print(f"{current_player} wins! GG!")
            return True

def Scanner(board): # Scans for the board after the first 9 move
    global var
    for i in board:
        for j in i:
            if j == ' _ ':
                var = False
                break
    if var == False:
        return False
    else:
        var = True

i = 2
while GameRun: 
    Print_board(board)
    if i%2 == 0:
        current_player = ' X '
        print(f"Player{current_player}to move:")
        i += 1
    else:
        current_player = ' O '
        print(f"Player{current_player}to move:")
        i += 1
        
    playerInput(board, current_player)
    a = WinLogic(board,row,col,current_player)
    if a is True:
        break
    elif i == 11:
        Scanner(board)
        if var:
            print("It's a draw!")
            break
