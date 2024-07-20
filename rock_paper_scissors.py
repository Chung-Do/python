import random
array_action = ["rock", "paper", "scissors"]
player1_action = input('player1 choice is ')
player2_action = input('player2 choice is ')
isValid = (player1_action in array_action) and (player2_action in array_action)
if (isValid == False):
    print('Error')
else:
    result = (player1_action == "rock" and player2_action == "scissors") or (player1_action == "paper" and player2_action == "rock") or (player1_action == "scissors" and player2_action == "paper")
    if player1_action == player2_action:
        print("It's a tie")
    elif (result):
        print("player1 wins")
    else:
        print("player2 wins")
