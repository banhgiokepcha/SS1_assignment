import random

def guessing_game(low, high):
    print('I have a screct number from', low, 'to', high)
    count = 0
    randNumber = random.randint(low, high)
    while(True):
        user_guess = int(input(('Guess a number (enter 0 to quit) ')))
        
        
        if (user_guess == 0):
         print('The secrect number is:', randNumber)
         print('Better luck next time')
         break
        if(user_guess > randNumber):
         print('You guessed too high!')
         count+=1
        elif(user_guess<randNumber):
         print('You guessed too low')  
         count+=1
        else: 
         count+=1
         break

    if(user_guess==randNumber):
        print('Congratulations you did it in', count, 'try')

guessing_game(1, 100)

        
     
