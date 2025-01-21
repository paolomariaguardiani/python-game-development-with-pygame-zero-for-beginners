# thanks to stackoverflow
x = 1920 // 2 - 753 // 2
y = 200
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = f'{x}, {y}'


import pgzrun

WIDTH = 753
HEIGHT = 800

def draw():
    screen.fill("blue")


def update():
    pass

pgzrun.go()