'''
To create the Rock, Paper and Scissors game with Python, we need to take the user’s choice and 
then we need to compare it with the computer choice which is taken using the random module in Python 
from a list of choices, and if the user wins then the score will increase by 1:
'''
import random
choices = ["Rock", "Paper", "Scissors"]
computer = random.choice(choices)
player = False
cpu_score = 0
player_score = 0
while True:
    player = input("Rock, Paper or  Scissors?").capitalize()
    ## Conditions of Rock,Paper and Scissors
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
            cpu_score+=1
        else:
            print("You win!", player, "smashes", computer)
            player_score+=1
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
            cpu_score+=1
        else:
            print("You win!", player, "covers", computer)
            player_score+=1
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
            cpu_score+=1
        else:
            print("You win!", player, "cut", computer)
            player_score+=1
    elif player=='End':
        print("Final Scores:")
        print(f"CPU:{cpu_score}")
        print(f"Plaer:{player_score}")
        break

'''
output-
Rock, Paper or  Scissors?rock
You win! Rock smashes Scissors
Rock, Paper or  Scissors?rock 
You win! Rock smashes Scissors
Rock, Paper or  Scissors?rock 
You win! Rock smashes Scissors
Rock, Paper or  Scissors?paper
You lose! Scissors cut Paper
Rock, Paper or  Scissors?scissors
Tie!
Rock, Paper or  Scissors?rock
You win! Rock smashes Scissors
Rock, Paper or  Scissors?end
Final Scores:
CPU:1
Plaer:4


Creating these types of games will help a beginner to think logically. You can even use this idea to make your own game.
'''