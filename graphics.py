from tkinter import Tk, BOTH, Canvas  #importing necessary libraries

class Window:  #create Window class

    def __init__(self, width, height):  #window constructor taking width and height, that creates and titles a window
        self.root = Tk()
        self.root.title("Tic-Tac-Toe")
        self.canvas = Canvas(self.root, bg = "white", height = height, width = width)
        self.canvas.pack(fill = BOTH, expand = True)
        self.running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        self.width = width
        self.height = height

    def redraw(self):  #redraw method that maintains the window when called
        self.root.update_idletasks()
        self.root.update()
    
    def wait_for_close(self):  #wait_for_close method continually calls redraw method until window is closed
        self.running = True
        while self.running == True:
            self.redraw()
        print("Window closed...")

    def close(self):  #close method removes the window
        self.running = False

    def draw_line(self, line, fill_color = "black"):  #draws a line in the window
        line.draw(self.canvas, fill_color)

class Point:  #create Point class
    def __init__(self, x, y):  #constructor stores point coordinates
        self.x = x
        self.y = y

class Line:  #create Line class
    def __init__(self, point_1, point_2):  #constructor takes and holds a pair of coordinates
        self.point_1 = point_1
        self.point_2 = point_2
        
    def draw(self, win, fill_color = "black"):  #draw method that creates a line between two points
        win.create_line(self.point_1.x, self.point_1.y, self.point_2.x, self.point_2.y, fill = fill_color, width = 2)

class Cell:  #create Cell class
    def __init__(self, win):  #constructor creating the variables for each cell
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.x1 = None
        self.x2 = None
        self.y1 = None
        self.y2 = None
        self.win = win
        self.filled = False

    def draw(self):  #draw method used to draw the borders of the cell if they exist
        if self.has_left_wall == True:
            line = Line(Point(self.x1, self.y1), Point(self.x1, self.y2))
            self.win.draw_line(line)
        if self.has_right_wall == True:
            line = Line(Point(self.x2, self.y1), Point(self.x2, self.y2))
            self.win.draw_line(line)
        if self.has_top_wall == True:
            line = Line(Point(self.x1, self.y1), Point(self.x2, self.y1))
            self.win.draw_line(line)
        if self.has_bottom_wall == True:
            line = Line(Point(self.x1, self.y2), Point(self.x2, self.y2))
            self.win.draw_line(line)

class Board:  #create Board class
    def __init__(self, win, point_1, point_2):  #constructor takes and holds opposite corners of the gameboard, then defines necessary x and y values based on those points before drawing out the board
        self.win = win
        self.x1 = point_1.x
        self.y1 = point_1.y
        self.x4 = point_2.x
        self.y4 = point_2.y
        self.x2 = (self.x4 - self.x1)/3 + self.x1
        self.x3 = self.x4 - (self.x4 - self.x1)/3
        self.y2 = (self.y4 - self.y1)/3 + self.y1
        self.y3 = self.y4 - (self.y4 - self.y1)/3

        self.create_cells()
        self.draw_cells()
        
    def create_cells(self):  #method for creating the cells that makeup the gameboard
        self.cells = []
        for j in range(0, 3):
            row_list = []
            for i in range(0, 3):
                row_list.append(Cell(self.win))
            self.cells.append(row_list)

    def draw_cells(self):  #method for defining and drawing the cells that makeup the gameboard
        for j in range(0, 3):
            for i in range(0, 3):
                if i == 0:
                    self.cells[i][j].has_left_wall = False
                    self.cells[i][j].x1 = self.x1
                    self.cells[i][j].x2 = self.x2
                if i == 1:
                    self.cells[i][j].x1 = self.x2
                    self.cells[i][j].x2 = self.x3
                if i == 2:
                    self.cells[i][j].has_right_wall = False
                    self.cells[i][j].x1 = self.x3
                    self.cells[i][j].x2 = self.x4
                if j == 0:
                    self.cells[i][j].has_top_wall = False
                    self.cells[i][j].y1 = self.y1
                    self.cells[i][j].y2 = self.y2
                if j == 1:
                    self.cells[i][j].y1 = self.y2
                    self.cells[i][j].y2 = self.y3
                if j == 2:
                    self.cells[i][j].has_bottom_wall = False
                    self.cells[i][j].y1 = self.y3
                    self.cells[i][j].y2 = self.y4
                self.cells[i][j].draw()
     