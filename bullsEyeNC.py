from graphics import *

def mk_circle(rad, cirX, cirY, color, win):
    bullRing = Circle(Point(cirX, cirY), rad)
    bullRing.setFill(color)
    bullRing.draw(win)

win = GraphWin("BullsEye", 750, 750)
win.setCoords(0, 0, 750, 750)

mk_circle(50, 375, 375, "hot pink", win)
