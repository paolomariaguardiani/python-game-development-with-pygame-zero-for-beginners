import pgzrun


def draw():
    square = Actor("square")
    square.anchor = ("left","top")
    square.pos = (300,300)
    square.draw()
    screen.draw.line((0,0), (300,300), color="red")


pgzrun.go()
