

import sys, random, pygame
# sys module provides access to system resources (i.e. Operating System Commands)

from pygame.locals import *
# Allows us to call functions from pygame using just the function name instead of modules.function()

# Constants for Game Board
BOARDWIDTH = 4 # COLUMNS
BOARDHEIGHT = 4 # ROWS
TILESIZE = 80 # WHAT UNIT DO YOU THINK THIS IS?
WINDOWWIDTH = 640 # MEASURED IN PIXELS
WINDOWHEIGHT = 480 # MEASURED IN PIXELS
FPS = 30 # this is a maximmum value! Won't make a slow computer run faster.
BLANK = None

# COLOR CALUES in (R, G, B) format.
# 0 = No Value, 225 = Max Value
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BRIGHTBLUE = (0, 50, 255)
DARKTURQUOISE = (3, 54, 73)
GREEN = (0, 204, 0)

# BOARD DESIGN SETUP
BGCOLOR = DARKTURQUOISE
TILECOLOR = GREEN
TEXTCOLOR = WHITE
BORDERCOLOR = BRIGHTBLUE
BASICFONTSIZE = 20 # pixels

# BUTTON SETUP
BUTTONCOLOR = WHITE
BUTTONTEXTXOLOR = BLACK
MESSAGECOLOR = WHITE

# ESTABLISH WINDOW MARGINS
XMARGIN = int((WINDOWWIDTH - (TILESIZE * BOARDWIDTH + (BOARDWIDTH -1))) / 2)
YMARGIN = int((WINDOWHEIGHT - (TILESIZE * BOARDHEIGHT + (BOARDHEIGHT -1))) / 2)

# Directions
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'