row1=[' ',' ',' ']
row2=[' ',' ',' ']
row3=[' ',' ',' ']

def display(row1, row2, row3):
    print (row1)
    print (row2)
    print (row3)

display(row1, row2, row3)
position_index=int(input('Choose a position:'))

def user_choice():
    #VARIABLES
    # initial values
    choice='hello'
    acceptable_values = range(0,10)
    within_range = False
    
    # TWO CONDITIONS TO CHECK
    # If choice is a digit or within the range
    while choice.isdigit()== False or within_range==False:
        choice= input('Enter a digit number (0-9): ')
        
        #DIGIT CHECK
        if choice.isdigit()== False:
            print('Sorry that is not a valid number')
            
        # RANGE CHECK
        if choice.isdigit()==True:
            if int(choice) in acceptable_values:
                within_range= True
            else:
                print('Sorry that number is not within the range of 1-9')
        
    return int(choice)