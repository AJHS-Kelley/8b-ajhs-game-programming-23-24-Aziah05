# Hangman game by Aziah Hill, v0.0
import random
words = 'chicken apple ugly nugget wild bad good something nothing want calm furious joy reveal blue purple yellow green red hot cold cool son mom dad uncle cousin aunt dry wet.'.split()
print(words)
# VARIABLE_NAMES IN ALL CAPS ARE CONSTANTS AND NOT MEANT TO CHANGE!
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
    # FINISH THURSDAY

# i = 0
# while i < 100:
#        word = getRandomWord(words)
#        print(word)
#        i += 1