from graphics import Window, Point, Board  #importing Window, Point and Board classes from graphics.py

width = 1000  #define initial variables for window size
height = 800

win = Window(width, height)  #create the window and then define variables to create the gameboard within the window
p1 = Point(width / 5, height / 5)
p2 = Point(4*width / 5, 4*height / 5)
board = Board(win, p1, p2)

win.wait_for_close()  #keeps the graphics running until game is closed