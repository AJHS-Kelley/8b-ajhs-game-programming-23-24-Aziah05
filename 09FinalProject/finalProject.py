# Final Project, Hill Aziah, v0.0
import sys, random, pygame

resolution = 0 # = Low Resolution (800, 600), 1 = High Resolution (1920, 1080)

screen = pygame.display.set_mode((x, y))
# CREAT AN if / else BLOCK TO SET RESOLUTION BASED ON THE VARIABLE ABOVE.

if resolution == 0:
    x = 800
    y = 600
else:
    x = 1920
    y = 1080

pygame.init()

def getDifficulty():
    difficulty = int(input("Please choose a difficulty. Enter 1 for EASY or 2 for HARD.\n"))
    if difficulty == 1:
        pygame.display.set_caption('NAME OF GAME -- EASY')
    else:
        pygame.display.set_caption('NAME OF GAME -- HARD')

screen = pygame.display.set_mode((x, y))

