# DICE GAME
import random
r = random.randint(1,6)
print(r)
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
    print("You're out of moves. Loser. Your current score is " + str(score))
