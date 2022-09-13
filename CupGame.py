import random

#Function to show the current game list

def display_game(game_list):
    print("Here is the current list: ")
    print(game_list)

#Function which accepts user input to select the player move

def position_choice():
    
    choice = 'wrong'
    
    while choice not in ['0','1','2']:
        
        choice = input("Pick a  position (0,1,2): ")
        
        if choice not in ['0','1','2']:
            print("Sorry, invalid choice! ")
            
    return int(choice)

#Function to modify the original game list based on the users input

def place_x(game_list,position):
    
    user_placement = 'X'
    
    game_list[position] = user_placement
    
    return game_list

#Function to confirm whether the user would like to play again. Use bool game_on below to control game running

def gameon_choice():
    
    choice = 'wrong'
    
    while choice.upper() not in ['Y','N']:
        
        choice = input("Keep playing? (Y,N): ")                       
        if choice.upper() not in ['Y','N']:
            print("Sorry, I dont understand, please choose Y or N")
                       
    if choice.upper() == 'Y':
        return True
    else:
        return False

def play():

    #Establishing variables to be used in game

    game_on = True
    game_list = [0,0,0]

    #Game logic using the above functions

    while game_on:
        
        display_game(game_list)
        
        position = position_choice()
        
        game_list = place_x(game_list,position)

        display_game(game_list)

        print("Now guess where I've shuffled the X!")

        random.shuffle(game_list)
        
        guess = position_choice()

        if game_list[guess] == 'X':
            display_game(game_list)
            print('Nice work!')
        else:
            display_game(game_list)
            print('You missed!')
        
        game_list = [0,0,0]
        game_on = gameon_choice()

    print('Thanks for playing the cup game!')