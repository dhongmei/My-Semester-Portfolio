#Daniel Mei
#1/6/2025
#Rock Paper Scissors

#Init
import random
wins = 0
losses = 0
ties = 0

#Functions
def game():
    wins = 0
    losses = 0
    ties = 0
    while True:
        print("Welcome to the Rock, Paper, Scissors Game") #player's choice
        player = input("Choose Rock, Paper, or Scissors: ")

        computer = random.randint(1,3)  #computer's choice
        if computer == 1:
            computer = "Paper"
        if computer == 2:
            computer = "Scissors"
        if computer == 3:
            computer = "Rock"

        if player == "Rock" and computer == "Scissors": #determines outcome
            print("You Win")
            wins = wins + 1
        elif player == "Rock" and computer == "Paper":
            print("You Lose")
            losses = losses + 1
        elif player == "Paper" and computer == "Scissors":
            print("You Lose")
            losses = losses + 1
        elif player == "Paper" and computer == "Rock":
            print("You Win")
            wins = wins + 1
        elif player == "Scissors" and computer == "Rock":
            print("You Lose")
            losses = losses + 1
        elif player == "Scissors" and computer == "Paper":
            print("You Win")
            wins = wins + 1
        elif player == computer:
            print("Tied")
            ties = ties + 1

        print("Wins: " + str(wins)) #displays scores
        print("Losses: " + str(losses))
        print("Ties: " + str(ties))

        play = input("Would you like to continue: ") #asks if user would like to continue
        if play == "Yes":
            print("Good Luck")
        if play == "No":
            break
#Main
game()
