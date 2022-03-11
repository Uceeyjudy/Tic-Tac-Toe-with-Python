game_list=[0,1,2]
def display_game(game_list):
    print('Here is the current list')
    print(game_list)
    

def position_choice():
    choice='wrong'
    while choice not in ['0', '1', '2']:
        choice=input('Pick a value (0,1,2): ')
        if choice not in ['0', '1', '2']:
            print('Sorry your choice is invalid')
            
    return int(choice)

def replacement_choice(game_list, position):
    
    user_replacement = input('Type a word to replace the position chosen')
    
    game_list[position]= user_replacement
    
    return game_list

def game_on():
    choice='wrong'
    while choice not in ['y','n']:
        choice=input('Do you want to keep playing? (y or n): ')
        if choice not in ['y','n']:
            print('Please make a choice y or n')
            
    if choice =='y':
        return True
    else:
        return False

game=True
game_list=[0,1,2]

while game:
    display_game(game_list)
    
    position = position_choice()
    
    game_list = replacement_choice(game_list, position)
    
    display_game(game_list)
    
    game = game_on()