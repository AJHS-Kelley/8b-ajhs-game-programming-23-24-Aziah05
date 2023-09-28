# Select the secret number from a given range.
# Player must guess the number.
# Compare guess to the secret number.
# What happens first the guess is wrong?
    # Tell them the guess is wrong.
    # Tell them the number of guesses left.
    # Tell them if too high / too low.
# What happens if the guess is right?
    # Tell them that the guess is correct.
    # Award a point.
# What happen is the player runs out of guesses?
    # Tell them that they lost the round.
    # Award point to CPU.
# Check to see if the player or CPU has >= 3 points, if so then they win.

import random # Import the random module to our code.

# DECLARATIONS
secretNumber = 10
playerGuess = -1
playerScore = 0
cpuScore = 0
numGuesses = 0
playerName = ""
difficulty = "Normal"
rangeMin = -1
rangeMax = -1
numAttempts = -1

print("""
      *~~~~~~~~~~~~~~~~~~~~~*
      |                     |
      |                     |
      |    Guess a Number   |
      |     Aziah Hill      |
      |                     |
      *~~~~~~~~~~~~~~~~~~~~~*
    """)

# CPU SECRET NUMBER GENERATION
secretNumber = random.randint(0,20)
print(secretNumber)

# GAME LOOP
print("You need to guess a number between 0 and 20 and you have 3 guesses.\nIf you guess it right, you get a point.\nIf you cant get it in three guess, the CPU gets a point.")

# ADD CODE HERE TO CHANGE DIFFICULTY BETWEEN EACH MATCH.
# print () an explanation of your three difficulty levels.
# use input() to store difficulty in difficulty variable.
# assign values to numAttempts, rangeMin, and rangeMax based on choice

while playerScore != 3 and cpuScore != 3:
    # pass -- Tells Python to skip this block of code.

    print(f"Player Score: {playerScore}\nCPU Score: {cpuScore}.\n")
    secretNumber = random.randint(rangeMin, rangeMax)
    # ADD CODE HERE TO CHANGE DIFFICULTY BETWEEN EACH ROUND

    numGuesses = 0
    for guesses in range(3):
        print(f"You have {3 - numGuesses} guesses remaining.\n")
        playerGuess = int(input("Type a number from 0 to 20 and press ENTER.\n"))
        # input() saves all data as a STRING by default.
        # int() will convert to an INTEGER
        # float() will convert to a FLOAT
        print(f"You have chosen {playerGuess}. Let's see if you're right!\n")
        if playerGuess == secretNumber:
            print("whoa dude, what a guess! You got it!\n")
            playerScore += 1
            break # IMMEDIATELY EXIT ANY LOOP YOU ARE IN!
        else:
            print("You didnt guess correctly.\n")
            if playerGuess > secretNumber:
                print("Your guess is too high.\n")
            else:
                print("Your guess is too low.\n")
        numGuesses += 1
    if playerGuess != secretNumber:
        cpuScore += 1
        print("The CPU wins a point since you ran out of guesses.\n")
    
    print("You've won due to scoring 3 points first!\n")
else:
    print("You lost twin, to a computer at that man.\n")
