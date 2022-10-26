import random
print("Welcome To TicTacToe!")
print("To make moves, you would need to enter a number from 1 to 9")
print("if you enter a wrong argument, a move is randomly chosen and played")

comp = input("Do you want to play against computer (Type y for yes, anything else to continue): ")

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
# lists = []

def Print_board(board): # Creates the Board for TicTacToe
    print("-------------------")
    print(f"| {board[0][0]} | {board[0][1]} | {board[0][2]} |")
    print("-------------------")
    print(f"| {board[1][0]} | {board[1][1]} | {board[1][2]} |")
    print("-------------------")
    print(f"| {board[2][0]} | {board[2][1]} | {board[2][2]} |")
    print("-------------------")


if comp == 'y':
   def CompInt(board): # Scans and makes move for the computer
        global row
        global col
        lists = []
        lis = []
        global Y_Axis
        global X_Axis
        for i in board:
             for coords,slot in enumerate(i):
                  if slot == ' _ ':
                      lis = (coords, board.index(i))
                      lists.append(lis)
                  elif slot == ' X ' or ' O ':
                       continue
    #     print(lists)
        length = len(lists) - 1
        if length <= 0:
            print("It's a draw")
            exit()
        else:               
            choose = random.randint(0,length)
        Y_Axis = lists[choose][1] 
        X_Axis = lists[choose][0]
        row = Y_Axis 
        col = X_Axis
        board[Y_Axis][X_Axis] = ' O '

        return Y_Axis, X_Axis

def playerInput(board, current_player): # Takes Input from the user

    global player
    global Place
    try:
        player = int(input("Enter the number from 1-9: "))
        if player > 9 or player < 1:
            player = random.randint(1,9)
    except:
        player = random.randint(1,9)
    finally:
        global row
        row = (player - 1)//3
        global col
        col = (player - 1) %3
        if board[row][col] == ' _ ':
            board[row][col] = current_player
            Place = False
            return Place
        else:
            print("That slot is occupied, go again")
            Place = True
            return Place
    
def WinLogic(board, row, col, current_player): # Decides who won the game

        if board[row][0] == board[row][1] == board[row][2] == current_player:
            Print_board(board)
            print(f"{current_player} wins! GG!")
            return True

        if board[0][col] == board[1][col] == board[2][col] == current_player:
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
        if comp == 'y':
            current_player = ' O '
            print("It's computer's turn")
            CompInt(board)
            i += 1
        else:
            current_player = ' O '
            print(f"Player{current_player}to move:")
            i += 1
       
    if comp == 'y' and i%2 == 0:
        pass
    else:        
        playerInput(board, current_player)
        if Place:
            while Place:
                playerInput(board, current_player)

    a = WinLogic(board,row,col,current_player)
    if i == 4 and comp == 'y':
        a = WinLogic(board,Y_Axis, X_Axis, current_player)   
    if a is True:
        break
    elif i == 11:
        Scanner(board)
        if var:
            print("It's a draw!")
            break
