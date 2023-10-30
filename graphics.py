from tkinter import Tk, BOTH, Canvas, Label  #importing from tkinter library

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

width = 1000  #define initial variables for window size and create window
height = 800
win = Window(width, height)

class Point:  #create Point class
    def __init__(self, x, y):  #constructor stores point coordinates
        self.x = x
        self.y = y

p1 = Point(width / 5, height / 5)  #define points used for gameboard creation
p2 = Point(4 * width / 5, 4 * height / 5)

class Line:  #create Line class
    def __init__(self, point_1, point_2):  #constructor takes and holds a pair of coordinates
        self.point_1 = point_1
        self.point_2 = point_2
        
    def draw(self, win, fill_color = "black"):  #draw method that creates a line between two points
        win.create_line(self.point_1.x, self.point_1.y, self.point_2.x, self.point_2.y, fill = fill_color, width = 4)

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
     
board = Board(win, p1, p2)  #define the gameboard

class Scoreboard:  #creates the scoreboard class
    def __init__(self, name2 = "Computer"):  #constructor for the scoreboard that holds default names and scores for the player(s)
        self.name1 = "Player 1"
        self.name2 = name2
        self.turn = self.name1
        self.score1 = 0
        self.score2 = 0

    def create_scoreboard(self):  #scoreboard creating function that creates a label for each player to display their score and a label telling who's turn it is
        player1_name = Label(win.root, text = self.name1, bg = "White", fg = "Blue", font = ("Arial", 20, "bold", "underline"))
        player1_name.place(x = 25, y = 10)
        player2_name = Label(win.root, text = self.name2, bg = "White", fg = "Red", font = ("Arial", 20, "bold", "underline"))
        player2_name.place(x = 825, y = 10)
        player1_score = Label(win.root, text = self.score1, bg = "White", fg = "Blue", font = ("Arial", 20, "bold"))
        player1_score.place(x = 75, y = 50)
        player2_score = Label(win.root, text = self.score2, bg = "White", fg = "Red", font = ("Arial", 20, "bold"))
        player2_score.place(x = 885, y = 50)
        player_turn = Label(win.root, text = f"{self.turn}'s turn!", bg = "White", fg = "Green", font = ("Arial", 30, "bold"))
        player_turn.place(x = 300, y = 25)