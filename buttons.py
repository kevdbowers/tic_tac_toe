from graphics import win, board, Scoreboard  #importing variables and a class from graphics.py
from tkinter import Button  #importing from tkinter library

def fill_board():  #function that places interactable buttons in each of the gameboard squares
    button00.place(x = board.x1 + 5, y = board.y1 + 5)
    button10.place(x = board.x2 + 5, y = board.y1 + 5)
    button20.place(x = board.x3 + 5, y = board.y1 + 5)
    button01.place(x = board.x1 + 5, y = board.y2 + 5)
    button11.place(x = board.x2 + 5, y = board.y2 + 5)
    button21.place(x = board.x3 + 5, y = board.y2 + 5)
    button02.place(x = board.x1 + 5, y = board.y3 + 5)
    button12.place(x = board.x2 + 5, y = board.y3 + 5)
    button22.place(x = board.x3 + 5, y = board.y3 + 5)

def players1_button_command():  #function that activates when the players1 button is selected to modify game settings for a single player
    players1_button.place_forget()
    players2_button.place_forget()
    board.draw_cells()

    global scoreboard
    scoreboard = Scoreboard()
    scoreboard.create_scoreboard()
    fill_board()

def players2_button_command():  #function that activates when the players2 button is selected to modify game settings for two players
    players2_button.place_forget()
    players1_button.place_forget()
    board.draw_cells()

    global scoreboard
    scoreboard = Scoreboard("Player 2")
    scoreboard.create_scoreboard()
    fill_board()

### A series of button functions corresponding to the cell in which the button is located that activate when a button is selected, remove the button, then occupy the cell and update the scoreboard as necessary
def board_select00():
    button00.place_forget()
    if scoreboard.turn == scoreboard.name1:
        board.draw_x(board.x1 + 30, board.y1 + 18, board.x2 - 30, board.y2 - 18)
        board.cells[0][0].filled = 1
    if scoreboard.turn == scoreboard.name2:
        board.draw_o(board.x1 + 30, board.y1 + 18, board.x2 - 30, board.y2 - 18)
        board.cells[0][0].filled -1
    scoreboard.update_scoreboard()

def board_select10():
    button10.place_forget()
    if scoreboard.turn == scoreboard.name1:
        board.draw_x(board.x2 + 30, board.y1 + 18, board.x3 - 30, board.y2 - 18)
        board.cells[1][0].filled = 1
    if scoreboard.turn == scoreboard.name2:
        board.draw_o(board.x2 + 30, board.y1 + 18, board.x3 - 30, board.y2 - 18)
        board.cells[1][0].filled = -1
    scoreboard.update_scoreboard()

def board_select20():
    button20.place_forget()
    if scoreboard.turn == scoreboard.name1:
        board.draw_x(board.x3 + 30, board.y1 + 18, board.x4 - 30, board.y2 - 18)
        board.cells[2][0].filled = 1
    if scoreboard.turn == scoreboard.name2:
        board.draw_o(board.x3 + 30, board.y1 + 18, board.x4 - 30, board.y2 - 18)
        board.cells[2][0].filled = -1
    scoreboard.update_scoreboard()

def board_select01():
    button01.place_forget()
    if scoreboard.turn == scoreboard.name1:
        board.draw_x(board.x1 + 30, board.y2 + 18, board.x2 - 30, board.y3 - 18)
        board.cells[0][1].filled = 1
    if scoreboard.turn == scoreboard.name2:
        board.draw_o(board.x1 + 30, board.y2 + 18, board.x2 - 30, board.y3 - 18)
        board.cells[0][1].filled = -1
    scoreboard.update_scoreboard()

def board_select11():
    button11.place_forget()
    if scoreboard.turn == scoreboard.name1:
        board.draw_x(board.x2 + 30, board.y2 + 18, board.x3 - 30, board.y3 - 18)
        board.cells[1][1].filled = 1
    if scoreboard.turn == scoreboard.name2:
        board.draw_o(board.x2 + 30, board.y2 + 18, board.x3 - 30, board.y3 - 18)
        board.cells[1][1].filled = -1
    scoreboard.update_scoreboard()

def board_select21():
    button21.place_forget()
    if scoreboard.turn == scoreboard.name1:
        board.draw_x(board.x3 + 30, board.y2 + 18, board.x4 - 30, board.y3 - 18)
        board.cells[2][1].filled = 1
    if scoreboard.turn == scoreboard.name2:
        board.draw_o(board.x3 + 30, board.y2 + 18, board.x4 - 30, board.y3 - 18)
        board.cells[2][1].filled = -1
    scoreboard.update_scoreboard()

def board_select02():
    button02.place_forget()
    if scoreboard.turn == scoreboard.name1:
        board.draw_x(board.x1 + 30, board.y3 + 18, board.x2 - 30, board.y4 - 18)
        board.cells[0][2].filled = 1
    if scoreboard.turn == scoreboard.name2:
        board.draw_o(board.x1 + 30, board.y3 + 18, board.x2 - 30, board.y4 - 18)
        board.cells[0][2].filled = -1
    scoreboard.update_scoreboard()

def board_select12():
    button12.place_forget()
    if scoreboard.turn == scoreboard.name1:
        board.draw_x(board.x2 + 30, board.y3 + 18, board.x3 - 30, board.y4 - 18)
        board.cells[1][2].filled = 1
    if scoreboard.turn == scoreboard.name2:
        board.draw_o(board.x2 + 30, board.y3 + 18, board.x3 - 30, board.y4 - 18)
        board.cells[1][2].filled = -1
    scoreboard.update_scoreboard()

def board_select22():
    button22.place_forget()
    if scoreboard.turn == scoreboard.name1:
        board.draw_x(board.x3 + 30, board.y3 + 18, board.x4 - 30, board.y4 - 18)
        board.cells[2][2].filled = 1
    if scoreboard.turn == scoreboard.name2:
        board.draw_o(board.x3 + 30, board.y3 + 18, board.x4 - 30, board.y4 - 18)
        board.cells[2][2].filled = -1
    scoreboard.update_scoreboard()

players1_button = Button(win.root, text = "1 Player", bg = "Blue", font = ("Arial", 20, "bold"), height = 3, width = 9, command = players1_button_command)  #creating the homepage buttons to select number of players
players2_button = Button(win.root, text = "2 Players", bg = "Red", font = ("Arial", 20, "bold"), height = 3, width = 9, command = players2_button_command)

button00 = Button(win.root, bg = "Light Grey", height = 8, width = 18, command = board_select00)  #creating the buttons used to fill in the gameboard
button01 = Button(win.root, bg = "Light Grey", height = 8, width = 18, command = board_select01)
button02 = Button(win.root, bg = "Light Grey", height = 8, width = 18, command = board_select02)
button10 = Button(win.root, bg = "Light Grey", height = 8, width = 18, command = board_select10)
button11 = Button(win.root, bg = "Light Grey", height = 8, width = 18, command = board_select11)
button12 = Button(win.root, bg = "Light Grey", height = 8, width = 18, command = board_select12)
button20 = Button(win.root, bg = "Light Grey", height = 8, width = 18, command = board_select20)
button21 = Button(win.root, bg = "Light Grey", height = 8, width = 18, command = board_select21)
button22 = Button(win.root, bg = "Light Grey", height = 8, width = 18, command = board_select22)