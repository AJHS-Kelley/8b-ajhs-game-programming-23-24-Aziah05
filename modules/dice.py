# Dice Rolling Module by Aziah Hill, v0,0
import random

def rollDice(numDice, sizeDice):
    numRolled = 0
    sum = 0
    while numRolled < numDice:
        roll = random.randint(1, sizeDice)
        sum += roll
        print(f"Roll: {roll}\n")
        print(f"Sum: {roll}\n")
        numRolled += 1
    return sum