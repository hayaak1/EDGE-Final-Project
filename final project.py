# DICE GAME
play_again = "yes"
while play_again == "yes":
    import random
    r = random.randint(1,6)

    score = 0
    for x in range (2):
        x = int(input("A die is rolled. Guess the number between 1-6: "))
        if x == r:
            score = score + 100
            print("You got it! Your current score is " + str(score))
            break
        else:
            score = score - 50
            if x !=  r:
                print("Wrong.")
    if x != r:
        print("You're out of moves. Your current score is " + str(score))


# COLOR GAME
    import random
    colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
    z = random.choice(colors)

    guess_color = input("\n\nGuess a color from the rainbow (red, orange, yellow, green, blue, indigo, violet): ")

    while guess_color != z:
            score = score - 50
            print("Wrong!!. Your current score is " + str(score))
            break
    if guess_color ==  z:
            score = score + 50
            print("You got it! Your current score is " + str(score))


# ROCK PAPER SCISSORS

    import random
    options = ["rock","paper","scissors"]
    computer = random.choice(options)

    print("You are player 1 \n(Type 'exit' to leave the game)")
    user = input("\n\nEnter your choice: rock, paper or scissors? ")



    if user == computer:
        print(" both players selected "  + user )

    elif user == "paper":
        if computer == "rock":
            print("**player 2 chose rock** \nYOU WON!! :)")
            score = score + 100
            print("Your current score is " + str(score))
        else:
            print("**player 2 chose scissors** \nYOU LOST!! :(")
            score = score - 100
            print("Your current score is " + str(score))

    elif user == "rock":
        if computer == "scissors":
            print("**player 2 chose scissors** \nYOU WON!! :)")
            score = score + 100
            print("Your current score is " + str(score))
        else:
            print("**player 2 chose paper** \nYOU LOST!! :(")
            score = score - 100
            print("Your current score is " + str(score))

    elif user == "scissors":
        if computer == "paper":
            print("**player 2 chose paper** \nYOU WON!! :)")
            score = score + 100
            print("Your current score is " + str(score))
        else:
            print("**player 2 chose rock **\nYOU LOST!! :(")
            score = score - 100
            print("Your current score is " + str(score))


    play_again = input("\n\nWant to play again?: ")