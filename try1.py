print("***************************GAMESTART***************************")
def Tic_Tac_Toe():
    c1 = 0
    c2 = 0
    c3 = 0
    c4 = 0
    c5 = 0
    c6 = 0
    c7 = 0
    c8 = 0
    c9 = 0
    c21 = 0
    c22 = 0
    c23 = 0
    c24 = 0
    c25 = 0
    c26 = 0
    c27 = 0
    c28 = 0
    c29 = 0
    #Storage for player 1
    player1storage = []
    #Storage for player 2
    player2storage = []
    for i in range(0,5):
        print("BOXES USED BY PLAYER 1 IS",player1storage)
        Player_1 = int(input("Player 1 Chance:"))
        player1storage.append(Player_1) #Stores the input values of player 1
        if player1storage[i] == 1:
            c1 += 1
        if player1storage[i] == 2:
            c2 += 1
        if player1storage[i] == 3:
            c3 += 1
        if player1storage[i] == 4:
            c4 += 1
        if player1storage[i] == 5:
            c5 += 1
        if player1storage[i] == 6:
            c6 += 1
        if player1storage[i] == 7:
            c7 += 1
        if player1storage[i] == 8:
            c8 += 1
        if player1storage[i] == 9:
            c9 += 1
        #This are the 8 possible wayplayer 1 can win
        winpos1 = c1 + c4 + c7 
        winpos2 = c2 + c5 + c8
        winpos3 = c3 + c6 + c9
        winpos4 = c1 + c2 + c3
        winpos5 = c4 + c5 + c6
        winpos6 = c7 + c8 + c9
        winpos7 = c1 + c5 + c9
        winpos8 = c3 + c5 + c7
        if winpos1 == 3 or winpos2 == 3 or winpos3 == 3 or winpos4 == 3 or winpos5 == 3 or winpos6 == 3 or winpos7 == 3 or winpos8 == 3:
            print("Player 1 is the winner")
            break
        #This if condition is used for breaking the loop afther the 9th chance
        if i==4:
            break
        Player_2 = int(input("Player 2 Chance:"))
        player2storage.append(Player_2)#This is the array whihc stoers the input from player 2
        if player2storage[i] == 1:
            c21 += 1
        if player2storage[i] == 2:
            c22 += 1
        if player2storage[i] == 3:
            c23 += 1
        if player2storage[i] == 4:
            c24 += 1
        if player2storage[i] == 5:
            c25 += 1
        if player2storage[i] == 6:
            c26 += 1
        if player2storage[i] == 7:
            c27 += 1
        if player2storage[i] == 8:
            c28 += 1
        if player2storage[i] == 9:
            c29 += 1
        #Possible way in whihc player 2 can win
        sum1 = c21 + c24 + c27
        sum2 = c25 + c22 + c28
        sum3 = c23 + c26 + c29
        sum4 = c21 + c22 + c23
        sum5 = c24 + c25 + c26
        sum6 = c23 + c25 + c27
        sum7 = c21 + c25 + c29
        sum8 = c27 + c28 + c29
        #Checking if player 2 is winner if not
        if sum1 == 3 or sum2 == 3 or sum3 == 3 or sum4 == 3 or sum5 == 3 or sum6 == 3 or sum7 == 3 or sum8 == 3:
            print("Player 2 is the winner")
            break
         #This statment is just for the user to know whihc are number /spaces which are already occuppied
        print("BOXES USED BY PLAYER 2 IS", player2storage)
     #This is condition to check weather the game is draw or not
    if sum1 != 3 and sum2 != 3 and sum3 != 3 and sum4 != 3 and sum5!=3 and sum6!=3 and sum7 != 3 and sum8 != 3 and winpos1!=3 and winpos2!=3 and winpos3 != 3 and winpos4!=3 and winpos5!=3 and winpos5!=3 and winpos6!=3 and winpos7!=3 and winpos8!=3:
        print("Match is Draw")

Tic_Tac_Toe()







