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

def empty_board():  #function that removes any buttons on the gameboard
    button00.place_forget()
    button10.place_forget()
    button20.place_forget()
    button01.place_forget()
    button11.place_forget()
    button21.place_forget()
    button02.place_forget()
    button12.place_forget()
    button22.place_forget()

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

###     A series of button functions corresponding to the cell in which the button is located that activate when a button is selected, remove the button,
###     then occupy the cell, check if anyone wins, update the scoreboard as necessary, then remove any remaining gameboard buttons and add a play_again button

def board_select00():
    global piece00_1, piece00_2
    button00.place_forget()
    if scoreboard.turn == scoreboard.name1:
        piece00_1, piece00_2 = board.draw_x(board.x1 + 30, board.y1 + 18, board.x2 - 30, board.y2 - 18)
        board.cells[0][0].filled = 1
    if scoreboard.turn == scoreboard.name2:
        piece00_1 = board.draw_o(board.x1 + 30, board.y1 + 18, board.x2 - 30, board.y2 - 18)
        piece00_2 = piece00_1
        board.cells[0][0].filled = -1
    winner = board.victory_check(scoreboard.turn, scoreboard.turn_count, board.cells[0][0])
    scoreboard.turn_count = scoreboard.update_scoreboard(scoreboard.turn_count, winner)
    if winner != None:
        empty_board()
        play_again_button.place(x = 400, y = 675)

def board_select10():
    global piece10_1, piece10_2
    button10.place_forget()
    if scoreboard.turn == scoreboard.name1:
        piece10_1, piece10_2 = board.draw_x(board.x2 + 30, board.y1 + 18, board.x3 - 30, board.y2 - 18)
        board.cells[1][0].filled = 1
    if scoreboard.turn == scoreboard.name2:
        piece10_1 = board.draw_o(board.x2 + 30, board.y1 + 18, board.x3 - 30, board.y2 - 18)
        piece10_2 = piece10_1
        board.cells[1][0].filled = -1
    winner = board.victory_check(scoreboard.turn, scoreboard.turn_count, board.cells[1][0])
    scoreboard.turn_count = scoreboard.update_scoreboard(scoreboard.turn_count, winner)
    if winner != None:
        empty_board()
        play_again_button.place(x = 400, y = 675)

def board_select20():
    global piece20_1, piece20_2
    button20.place_forget()
    if scoreboard.turn == scoreboard.name1:
        piece20_1, piece20_2 = board.draw_x(board.x3 + 30, board.y1 + 18, board.x4 - 30, board.y2 - 18)
        board.cells[2][0].filled = 1
    if scoreboard.turn == scoreboard.name2:
        piece20_1 = board.draw_o(board.x3 + 30, board.y1 + 18, board.x4 - 30, board.y2 - 18)
        piece20_2 = piece20_1
        board.cells[2][0].filled = -1
    winner = board.victory_check(scoreboard.turn, scoreboard.turn_count, board.cells[2][0])
    scoreboard.turn_count = scoreboard.update_scoreboard(scoreboard.turn_count, winner)
    if winner != None:
        empty_board()
        play_again_button.place(x = 400, y = 675)

def board_select01():
    global piece01_1, piece01_2
    button01.place_forget()
    if scoreboard.turn == scoreboard.name1:
        piece01_1, piece01_2 = board.draw_x(board.x1 + 30, board.y2 + 18, board.x2 - 30, board.y3 - 18)
        board.cells[0][1].filled = 1
    if scoreboard.turn == scoreboard.name2:
        piece01_1 = board.draw_o(board.x1 + 30, board.y2 + 18, board.x2 - 30, board.y3 - 18)
        piece01_2 = piece01_1
        board.cells[0][1].filled = -1
    winner = board.victory_check(scoreboard.turn, scoreboard.turn_count, board.cells[0][1])
    scoreboard.turn_count = scoreboard.update_scoreboard(scoreboard.turn_count, winner)
    if winner != None:
        empty_board()
        play_again_button.place(x = 400, y = 675)

def board_select11():
    global piece11_1, piece11_2
    button11.place_forget()
    if scoreboard.turn == scoreboard.name1:
        piece11_1, piece11_2 = board.draw_x(board.x2 + 30, board.y2 + 18, board.x3 - 30, board.y3 - 18)
        board.cells[1][1].filled = 1
    if scoreboard.turn == scoreboard.name2:
        piece11_1 = board.draw_o(board.x2 + 30, board.y2 + 18, board.x3 - 30, board.y3 - 18)
        piece11_2 = piece11_1
        board.cells[1][1].filled = -1
    winner = board.victory_check(scoreboard.turn, scoreboard.turn_count, board.cells[1][1])
    scoreboard.turn_count = scoreboard.update_scoreboard(scoreboard.turn_count, winner)
    if winner != None:
        empty_board()
        play_again_button.place(x = 400, y = 675)

def board_select21():
    global piece21_1, piece21_2
    button21.place_forget()
    if scoreboard.turn == scoreboard.name1:
        piece21_1, piece21_2 = board.draw_x(board.x3 + 30, board.y2 + 18, board.x4 - 30, board.y3 - 18)
        board.cells[2][1].filled = 1
    if scoreboard.turn == scoreboard.name2:
        piece21_1 = board.draw_o(board.x3 + 30, board.y2 + 18, board.x4 - 30, board.y3 - 18)
        piece21_2 = piece21_1
        board.cells[2][1].filled = -1
    winner = board.victory_check(scoreboard.turn, scoreboard.turn_count, board.cells[2][1])
    scoreboard.turn_count = scoreboard.update_scoreboard(scoreboard.turn_count, winner)
    if winner != None:
        empty_board()
        play_again_button.place(x = 400, y = 675)

def board_select02():
    global piece02_1, piece02_2
    button02.place_forget()
    if scoreboard.turn == scoreboard.name1:
        piece02_1, piece02_2 = board.draw_x(board.x1 + 30, board.y3 + 18, board.x2 - 30, board.y4 - 18)
        board.cells[0][2].filled = 1
    if scoreboard.turn == scoreboard.name2:
        piece02_1 = board.draw_o(board.x1 + 30, board.y3 + 18, board.x2 - 30, board.y4 - 18)
        piece02_2 = piece02_1
        board.cells[0][2].filled = -1
    winner = board.victory_check(scoreboard.turn, scoreboard.turn_count, board.cells[0][2])
    scoreboard.turn_count = scoreboard.update_scoreboard(scoreboard.turn_count, winner)
    if winner != None:
        empty_board()
        play_again_button.place(x = 400, y = 675)

def board_select12():
    global piece12_1, piece12_2
    button12.place_forget()
    if scoreboard.turn == scoreboard.name1:
        piece12_1, piece12_2 = board.draw_x(board.x2 + 30, board.y3 + 18, board.x3 - 30, board.y4 - 18)
        board.cells[1][2].filled = 1
    if scoreboard.turn == scoreboard.name2:
        piece12_1 = board.draw_o(board.x2 + 30, board.y3 + 18, board.x3 - 30, board.y4 - 18)
        piece12_2 = piece12_1
        board.cells[1][2].filled = -1
    winner = board.victory_check(scoreboard.turn, scoreboard.turn_count, board.cells[1][2])
    scoreboard.turn_count = scoreboard.update_scoreboard(scoreboard.turn_count, winner)
    if winner != None:
        empty_board()
        play_again_button.place(x = 400, y = 675)

def board_select22():
    global piece22_1, piece22_2
    button22.place_forget()
    if scoreboard.turn == scoreboard.name1:
        piece22_1, piece22_2 = board.draw_x(board.x3 + 30, board.y3 + 18, board.x4 - 30, board.y4 - 18)
        board.cells[2][2].filled = 1
    if scoreboard.turn == scoreboard.name2:
        piece22_1 = board.draw_o(board.x3 + 30, board.y3 + 18, board.x4 - 30, board.y4 - 18)
        piece22_2 = piece22_1
        board.cells[2][2].filled = -1
    winner = board.victory_check(scoreboard.turn, scoreboard.turn_count, board.cells[2][2])
    scoreboard.turn_count = scoreboard.update_scoreboard(scoreboard.turn_count, winner)
    if winner != None:
        empty_board()
        play_again_button.place(x = 400, y = 675)

def play_again_button_command():  #command for the play_again button that clears the gameboard and resets round specific variables, built with error exceptions to test functionality but needs to be simplified
    play_again_button.place_forget()
    board.empty_cells()
    try:
        win.canvas.delete(piece00_1)
        win.canvas.delete(piece00_2)
        raise Exception()
    except Exception as error:
        pass
    try:
        win.canvas.delete(piece10_1)
        win.canvas.delete(piece10_2)
        raise Exception()
    except Exception as error:
        pass
    try:
        win.canvas.delete(piece20_1)
        win.canvas.delete(piece20_2)
        raise Exception()
    except Exception as error:
        pass
    try:
        win.canvas.delete(piece01_1)
        win.canvas.delete(piece01_2)
        raise Exception()
    except Exception as error:
        pass
    try:
        win.canvas.delete(piece11_1)
        win.canvas.delete(piece11_2)
        raise Exception()
    except Exception as error:
        pass
    try:
        win.canvas.delete(piece21_1)
        win.canvas.delete(piece21_2)
        raise Exception()
    except Exception as error:
        pass
    try:
        win.canvas.delete(piece02_1)
        win.canvas.delete(piece02_2)
        raise Exception()
    except Exception as error:
        pass
    try:
        win.canvas.delete(piece12_1)
        win.canvas.delete(piece12_2)
        raise Exception()
    except Exception as error:
        pass
    try:
        win.canvas.delete(piece22_1)
        win.canvas.delete(piece22_2)
        raise Exception()
    except Exception as error:
        pass
    board.victory_label.place_forget()
    scoreboard.turn = scoreboard.name1
    scoreboard.turn_count = 0
    fill_board()

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

play_again_button = Button(win.root, text = "Play Again", bg = "Green", font = ("Arial", 20, "bold"), height = 2, width = 9, command = play_again_button_command)