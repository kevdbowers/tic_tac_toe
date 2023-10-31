from graphics import win  #importing necessary variables from graphics.py
from buttons import players1_button, players2_button  #importing necessary variables from buttons.py

def main():  #the main function that runs our program
    players1_button.place(x = 200, y = 300)  #placing the initial buttons to choose how many players there are
    players2_button.place(x = 600, y = 300)
    
    win.wait_for_close()  #keeps the graphics running until game is closed

main()  #running our main function