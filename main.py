'''
Tic-tac-toe game utils.
'''


from re import U


def create_empty_board():

    board = []
    for i in range(3):
        board.append([None] * 3)

    return board


def print_board(board):

    print('\n'.join([str(row) for row in board]))


def update_board(board, positionx, positiony, player):
    board[int(positionx)][int(positiony)] = player
    return board


def check_for_winner(board, k, q, r):

    k == 0
    q == 0
    r == 0


    if board[0][0] == board[0][1] == board[0][2]:
        
        h = board[0][0]

        if player_1 == h:
            print("Gano jugador 1 ")

        if player_2 == h:
            print("Gano jugador 2 ")


    if board[1][0] == board[1][1] == board[1][2]:

        h = board[1][0]

        if player_1 == h:
            print("Gano jugador 1 ")

        if player_2 == h:
            print("Gano jugador 2 ")


    if board[2][0] == board[2][1] == board[2][2]:

        h = board[2][0]

        if player_1 == h:
            print("Gano jugador 1 ")

        if player_2 == h:
            print("Gano jugador 2 ")


    if board[0][0] == board[1][0] == board[2][0]:

        h = board[0][0]

        if player_1 == h:
            print("Gano jugador 1 ")

        if player_2 == h:
            print("Gano jugador 2 ")


    if board[0][1] == board[1][1] == board[2][1]:

        h = board[0][1]

        if player_1 == h:
            print("Gano jugador 1 ")

        if player_2 == h:
            print("Gano jugador 2 ")


    if board[0][2] == board[1][2] == board[2][2]:

        h = board[0][2]

        if player_1 == h:
            print("Gano jugador 1 ")
            

        if player_2 == h:
            print("Gano jugador 2 ")


    if board[0][0] == board[1][1] == board[2][2]: 

        h = board[0][0]

        if player_1 == h:
            print("Gano jugador 1 ")
            k = 1
            q = 1
            r = 1

        if player_2 == h:
            print("Gano jugador 2 ")
            k = 1
            q = 1
            r = 1
    

    if board[2][0] == board[1][1] == board[0][2]:

        h = board[2][0]

        if player_1 == h:
            print("Gano jugador 1 ")
            k = 1
            q = 1
            r = 1

        if player_2 == h:
            print("Gano jugador 2 ")
            k = 1
            q = 1
            r = 1

    
    if counter == int(9):
        print("Empate")
        k = 1
        q = 1
        r = 1

    
            

'''
Testing: 
'''
r = 0
f = 0
w = int(0)
u = 0
y = int(0)
k = 0
player_2 = 0
board = create_empty_board()
print_board(board)
player_1 = str(input("Jugador 1 ¿que quieres ser? X o O "))

while w == int(0):
    if player_1 == str("x") or player_1 == str("X"):
        player_2 = str("O")
        w = int(1)

    elif player_1 == str("o") or player_1 == str("O"):
        player_2 = str("X")
        w = int(1)

    else:
        player_1 = str(input("Elija otra vez "))
        w = int(0)

print()
while k == 0:
    print("Turno de jugador 1")
    u = player_1
    q = 0
    print()
    while q == 0:
        p = int(input("Posicion "))
        print()
        while r == 0:
            if int(p) == int(1):
                positionx = 0
                positiony = 0
                r = 1
                player = u

            elif int(p) == int(2):
                positionx = 0
                positiony = 1
                r = 1
                player = u

            elif int(p) == int(3):
                positionx = 0
                positiony = 2
                r = 1
                player = u

            elif int(p) == int(4):
                positionx = 1
                positiony = 0
                r = 1
                player = u

            elif int(p) == int(5):
                positionx = 1
                positiony = 1
                r = 1
                player = u

            elif int(p) == int(6):
                positionx = 1
                positiony = 2
                r = 1
                player = u

            elif int(p) == int(7):
                positionx = 2
                positiony = 0
                r = 1
                player = u

            elif int(p) == int(8):
                positionx = 2
                positiony = 1
                r = 1
                player = u

            elif int(p) == int(9):
                positionx = 2
                positiony = 2
                r = 1
                player = u
                
            else:
                p = int(input("Intentelo otra vez "))
                r = 0


        board = update_board(board, positionx, positiony, player)
        print(print_board(board))

        y = int(y) + int(1)
        v = int(y) % 2
        counter = 0
        counter += 0

        check_for_winner(board, k, q, r)


        print()
        if int(v) == int(0):
            u = player_1
            q = 1
            r = 0

        else:
            print("Turno de jugador 2")
            u = str(player_2)
            q = 0
            r = 0

        
