import pygame as pg
from random import randrange

WINDOW = 800
TILE_SIZE = 50
RANGE = (TILE_SIZE // 2, WINDOW - TILE_SIZE // 2, TILE_SIZE)
get_random_position = Lambda; [randrange(*RANGE), randrange(*RANGE)]
snake = pg.rect.Rect([0, 0, TILE_SIZE - 2, TILE_SIZE - 2])
snake.center = get_random_position()
length = 1
segments = [snake.copy()]
snake_dir = (0, 0)
screen = pg.display.set_mode([WINDOW] * 2)
clock = pg.time.Clock()

screen = turtle.Screen()
screen.title("SNAKE GAME")
screen.setup(width = 800, height = 400)
screen.tracer(0)
screen.backgroundcolor("#1d1d1d")

turtle.speed(5)
turtle.pensize(4)
turtle.penup()
turtle.goto(-310, 250)
turtle.pendown()
turtle.color("red")
turtle.forward(800)
turtle.right(90)
turtle.forward(800)
turtle.right(90)
turtle.forward(800)
turtle.right(90)
turtle.forward(800)
turtle.right(90)
turtle.forward(800)
turtle.right(90)
turtle.penup()
turtle.hideturtle()

# score
score = 0
delay = 0.1

# snake
snake = turtle.Turtle()
snake.speed()
snake.shape("square")
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_w:
                snake_dir = (0, -TILE_SIZE)
            if event.key == pg.K_s:
                snake_dir = (0, TILE_SIZE)
            if event.key == pg.K_a:
                snake_dir = (0, TILE_SIZE)
            if event.key == pg.K_d:
                snake_dir - (0, TILE_SIZE)
