#rock paper scissors
import random
print("You are player 1 \n (Type 'exit' to leave the game)")
user = input("Enter your choice: rock, paper or scissors?")
options = ["rock","paper","scissors"]
computer = random.choice(options)

while user !="exit":

    if user == computer:
        print("TRY AGAIN, both players selected "  + user )
    elif user == "paper":
        if computer == "rock":
            print("**player 2 chose rock** \n YOU WON!! :)")
        else:
            print("**player 2 chose scissors** \n YOU LOST!! :(")


    elif user == "rock":
        if computer == "scissors":
            print("**player 2 chose scissors** \n YOU WON!! :)")
        else:
            print("**player 2 chose paper** \n YOU LOST!! :(")


    elif user == "scissors":
        if computer == "paper":
            print("**player 2 chose paper** \n YOU WON!! :)")
        else:
            print("**player 2 chose rock **\n YOU LOST!! :(")

    user = input("Play Again")


