from random import choice

def InitializeGrid(board):
    #Initialize Grid by reading in from file
    for i in range(8):
        for j in range(8):
            board[i][j] = choice(['Q', 'R', 'S', 'T', 'U'])

def Initialize(board):
    #Initialize game
    #Initialize grid
    InitializeGrid(board)
    #Initialize score
    global score
    score = 0
    #Initialize turn number
    global turn
    turn = 1

def ContinueGame(current_score, goal_score = 100):
    #Return false if game should end, true if game is not over
    if (current_score >= goal_score):
        return False
    else:
        return True

def DrawBoard(board):
    #Display the board to the screen
    linetodraw=""
    #Draw some blank lines first
    print("\n\n\n")
    print(" ------------------------------------")
    #Now draw rows from 8 down to 1
    for i in range(7,-1,-1):
        #draw each row
        linetodraw=""
        for j in range(8):
            linetodraw += " | " + board[i][j]
        linetodraw+= " | "
        print(linetodraw)
        print("-------------------------------------")

def GetMove():
    #Get the move from the user
    move = input("Enter move: ")
    print("Getting move")
    return move

def Update(board, move):
    #Update hte board according to move
    print("Updating board")

def DoRound(board):
    #Perform one round of the game
    #Display current board
    DrawBoard(board)
    #Get move
    move = GetMove()
    #Update board
    Update(board, move)
    #Update turn number
    global turn
    turn += 1

#State main variables
score = 100
turn = 100 
goalscore = 100
board = [[0,0,0,0,0,0,0,0], 
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0]]

#Initialize game
Initialize(board)

score = 50
goalscore = 100

#While game not over
while ContinueGame(score, goalscore):
    #Do a round of the game
    DoRound(board)