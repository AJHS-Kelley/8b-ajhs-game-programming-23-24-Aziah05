import turtle
import random
import time
import pygame


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
