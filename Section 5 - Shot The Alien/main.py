x = 100
y = 100
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = f'{x}, {y}'

import pgzrun
from random import randint

TITLE = "Shoot The Alien"
WIDTH = 800
HEIGHT = 600

message = ""

alien = Actor('alien') # type: ignore
# alien.pos = 50,50


def draw():
    screen.clear() # type: ignore
    screen.fill(color=(128,0,0)) # type: ignore
    alien.draw()
    screen.draw.text(message, center=(WIDTH/2, 40), fontsize=60)  # Il centro del testo è il centro della finestra
    # for i in range(10000):
    #     place_alien()
    #     alien.draw()


def place_alien():
    alien.x = randint(50, WIDTH-50)
    alien.y = randint(59, HEIGHT-50)


def on_mouse_down(pos):
    global message
    if alien.collidepoint(pos):  # here is correct collidepoint, not colliderect
        message = "Good Shot!"
        place_alien()
    else:
        message = "You missed!"



place_alien()
pgzrun.go()