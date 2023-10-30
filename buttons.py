from graphics import win, board, Scoreboard  #importing variables and a class from graphics.py
from tkinter import Button  #importing from tkinter library

def players1_button_command():  #function that activates when the players1 button is selected to modify game settings for a single player
    players1_button.place_forget()
    players2_button.place_forget()
    board.draw_cells()
    scoreboard = Scoreboard()
    scoreboard.create_scoreboard()

def players2_button_command():  #function that activates when the players2 button is selected to modify game settings for two players
    players2_button.place_forget()
    players1_button.place_forget()
    board.draw_cells()
    scoreboard = Scoreboard("Player 2")
    scoreboard.create_scoreboard()

players1_button = Button(win.root, text = "1 Player", bg = "Blue", font = ("Arial", 20, "bold"), height = 3, width = 9, command = players1_button_command)  #creating the homepage buttons to select number of players
players2_button = Button(win.root, text = "2 Players", bg = "Red", font = ("Arial", 20, "bold"), height = 3, width = 9, command = players2_button_command)