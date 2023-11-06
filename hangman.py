# Hangman game by Aziah Hill, v0.0
import random
# words = 'chicken apple ugly nugget wild bad good something nothing want calm furious joy reveal blue purple yellow green red hot cold cool son mom dad uncle cousin aunt dry wet.'.split()
# DICTIONARY VERSION
# stored in key: value pairs.
# Actual Dictionary Word (Key) : Value (Definition)
# Uses {} to specify a dictionary
words = {'Colors': 'red orange yellow green blue indigo violet teal gold black white silver fushia'.split(),
        'Animals': 'cat cow dog moose goose fish wombat wolverine giraffe hippo lion alligator'.split(),
        'Shapes': 'square triangle rectangle circle rhombas parallelogram trapezoid diamond rectangle'.split(),
        'Food': 'hamburger hotdog potato waffle pancake eggs steak salmon donut'.split()}


# VARIABLE_NAMES in ALL CAPS ARE CONSTANTS AND NOT MEANT TO CHANGE!
HANGMAN_BOARD = ['''
    +---+
        |
        |                 
        |
    =======''', '''
    +---+
    O   |
        |
        |
    =======''','''
     +---+
    O   |
    |   |
        |
    =======''','''
     +---+
    O   |
    |\  |
        |
    =======''','''
     +---+
    O   |
   /|\  |
        |
    =======''','''
     +---+
    O   |
   /|\  |
   /    |
    =======''','''
      +---+
    O   |
   /|\  |
   / \  |
    =======''']
   
# Pick Word from list
def getRandomWord(wordList): # Return a random word from the list.
    wordIndex = random.randint(0, len(wordList) - 1)
    # len(listName) - 1 is EXTREMELY COMMON FOR WORKING WITH LISTS.
    return wordList[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_BOARD[len(missedLetters)])
    print()

    print('Missed Letters:', end = ' ')
    for eachLetter in missedLetters:
        print(eachLetter, end =' ')
    print()
    
    blanks = '_' * len(secretWord)

    # Replace Blanks with Correct letters
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
    
    for letter in blanks:
        print(letter, end = ' ')
    print()


def getGuess(alreadyGuessed):
    while True:
        print('Please pick a letter from A to Z and hit Enter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('Letter has been guessed already, try again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please guess a LETTER from the Englsih alphabet.')
        else:
            return guess
        
def playAgain():
    print('Do you want to play again? Yes or No?')
    return input().lower().startwith('y')

# Introduce the game
print('Welcome to Hangman by Ryan K.')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

# Main game loop
while True:
    displayBoard(missedLetters, correctLetters, secretWord)

    guess = getGuess(missedLetters + correctLetters)

    if guess is secretWord:
        correctLetters = correctLetters + guess

        # Check to see if winner, winner chicken dinner
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
            if foundAllLetters: # if True
                print('Much wow! Very win! Well done.')
                print('The secret word was' + secretWord)
                gameIsDone = True
    else:
        missedLetters = missedLetters + guess
        
        if len(missedLetters) == len(HANGMAN_BOARD) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('You dont have anymore guesses and u took a L twin.')
            print('You mad this number of correct guesses ' + str(len(correctLetters)))
            print('The secret word was ' + secretWord)
            gameIsDone = True

    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord(words)
        else:
            break



# i = 0
# while i < 100:
#        word = getRandomWord(words)
#        print(word)
#        i += 1