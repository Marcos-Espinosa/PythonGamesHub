import CupGame
import TicTacToe
import os

def clear():
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
    
    #for mac and linux
    else:
        _ = os.system('clear')

def play_again():
    again = input('Would you like to play another game?')

    if again.lower() == 'y':
        clear()
        return True
    elif again.lower() == 'n':
        return False        

print('Welcome to the Python Games Hub!')
print("Here you can play some text based games that I've made in my learning journey")

playing = True

while playing:

    clear()
    selection = input('What game would you like to play? \n1. Cup Game\t2.Tic Tac Toe\n')
    clear()

    if selection == '1':
        CupGame.play()
    elif selection == '2':
        TicTacToe.play()
    else:
        print("Sorry that's not a valid selection")

    playing = play_again()

print('Thanks for checking out the Python Games Hub!')