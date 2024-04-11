# Final Project, Hill Aziah, v0.0
import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)

# Be sure to put the images your using inside of the FIRST SET of parentheses
sky_surface = pygame.image.load()()
ground_surface = pygame.image.load()()

score_surface = test_font.render('My game', False, (64,64,64))
score_rect = score_surface.get_rect(center = (400,50))

bird_surface = pygame.image.load('img/ultimatePygame/snail1.png').convert_alpha()
bird_rect = bird_surface.get_rect(bottomright = (600,300))

resolution = 0 # = Low Resolution (800, 600), 1 = High Resolution (1920, 1080)

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

