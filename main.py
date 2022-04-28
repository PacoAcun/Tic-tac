'''
Tic-tac-toe game utils.
'''


from re import U
from typing import Counter


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


def check_for_winner(board, counter, co):

    counter += 1
    print()

    if board[0][0] == board[0][1] == board[0][2] == str("x") or board[0][0] == board[0][1] == board[0][2] == str("X") or board[0][0] == board[0][1] == board[0][2] == str("O") or board[0][0] == board[0][1] == board[0][2] == str("O"):
        
        h = board[0][0]

        if player_1 == h:
            print("Gano jugador 1 ")
            counter = int(19)

        if player_2 == h:
            print("Gano jugador 2 ")
            counter = int(19)

    


    if board[1][0] == board[1][1] == board[1][2] == str("x") or board[1][0] == board[1][1] == board[1][2] == str("X") or board[1][0] == board[1][1] == board[1][2] == str("O") or board[1][0] == board[1][1] == board[1][2] == str("o"):

        h = board[1][0]

        if player_1 == h:
            print("Gano jugador 1 ")
            counter = int(19)

        if player_2 == h:
            print("Gano jugador 2 ")
            counter = int(19)

        


    if board[2][0] == board[2][1] == board[2][2] == str("x") or board[2][0] == board[2][1] == board[2][2] == str("X") or board[2][0] == board[2][1] == board[2][2] == str("O") or board[2][0] == board[2][1] == board[2][2] == str("o"):

        h = board[2][0]

        if player_1 == h:
            print("Gano jugador 1 ")
            counter = int(19)

        if player_2 == h:
            print("Gano jugador 2 ")
            counter = int(19)

        


    if board[0][0] == board[1][0] == board[2][0]:

        h = board[0][0]

        if player_1 == h:
            print("Gano jugador 1 ")
            counter = int(19)

        if player_2 == h:
            print("Gano jugador 2 ")
            counter = int(19)

        


    if board[0][1] == board[1][1] == board[2][1]:

        h = board[0][1]

        if player_1 == h:
            print("Gano jugador 1 ")
            counter = int(19)

        if player_2 == h:
            print("Gano jugador 2 ")
            counter = int(19)

        


    if board[0][2] == board[1][2] == board[2][2]:

        h = board[0][2]

        if player_1 == h:
            print("Gano jugador 1 ")
            counter = int(19)
            

        if player_2 == h:
            print("Gano jugador 2 ")
            counter = int(19)

        


    if board[0][0] == board[1][1] == board[2][2]: 

        h = board[0][0]

        if player_1 == h:
            print("Gano jugador 1 ")
            counter = int(19)
            

        if player_2 == h:
            print("Gano jugador 2 ")
            counter = int(19)
        
            
    

    if board[2][0] == board[1][1] == board[0][2]:

        h = board[2][0]

        if player_1 == h:
            print("Gano jugador 1 ")
            counter = int(19)
            

        if player_2 == h:
            print("Gano jugador 2 ")
            counter = int(19)

        
            

    
    if int(counter) == int(9):
        print("Empate")
        counter = int(19)
        board = create_empty_board()

    if int(counter) > int(9):
        co = False
        

    return co
        

    
            

'''
Testing: 
'''
r = 0
f = 0
w = int(0)
u = 0
l = int(0)
z = int(0)
y = int(0)
k = 0
co = True
counter = int(0)
player_2 = 0
board = create_empty_board()
print()
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
print_board(board)

while z == int(0):
    k = int(0)
    q = 0
    r = int(0)
    l = int(0)
    p = int(0)
    c_2 = 0
    print()

    while l == int(0):
        while k == int(0):
            if counter > int(9):
                print()
                board = create_empty_board()
                print_board(board)
                k = 1
                q = 1
                r = 1

            print()
            print("Turno de jugador 1")
            u = player_1
            q = 0

            while q == 0:
                p = int(input("Posicion "))
                print()
                r = int(0)
                while r == int(0):
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

                c_2 = 0
                y = int(y) + int(1)
                v = int(y) % 2

                co = check_for_winner(board, counter, co)

                if co == False:
                    print()
                    board = create_empty_board()
                    print_board(board)
                    k = 1
                    q = 1
                    r = 1
                    c_2 = 1
                    l = 1

                print()

                while c_2 == 0:
                    if int(v) == int(0):
                        u = player_1
                        q = 1
                        r = 0
                        c_2 = 1
                        l = 0

                    elif int(0) < int(v) or int(0) > int(v):
                        print("Turno de jugador 2")
                        u = str(player_2)
                        q = 0
                        r = 0
                        c_2 = 1
                        l = 0


    x = str(input("Quieres jugar otra vez?  Y/N: "))
    c_3 = int(0)

    while c_3 == int(0):
        if str(x) == str("Y") or str(x) == str("y") or str(x) == str("N") or str(x) == str("n"):
            k = 0
            q = 0
            r = 0
            c_3 += int(1)

        else:
            x = str(input("Responde otra vez Y/N: "))
            k = int(1)
            q = 1
            r = int(1)
            l = int(1)
            p = int(1)
            c_2 = 1
            z = 1

        
