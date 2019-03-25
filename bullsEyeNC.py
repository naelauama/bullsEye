from graphics import *
from random import *

def mk_circle(rad, cirX, cirY, color, win):
    bullRing = Circle(Point(cirX, cirY), rad)
    bullRing.setFill(color)
    bullRing.draw(win)

rad = randint(10, 100)
cirXY = randint(200, 400)
color = color_rgb(randint(0, 255), randint(0, 255), randint(0, 255))

win = GraphWin("BullsEye", 750, 750)
win.setCoords(0, 0, 750, 750)

mk_circle(rad, cirXY, cirXY, color, win)
