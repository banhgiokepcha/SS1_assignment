def myGuess():
    print('Please pick a random number from 1 to 100 and keep it a secret. I will try to guess your number !')
    low_range = 1
    high_range= 100
    guess = (high_range + low_range - 1) / 2 
    count = 0;
    while (True): 
        guess = int((high_range + low_range - 1) / 2)
        count += 1
        print('Is', guess, 'your number?')
        user_input = input('Enter c if it is correct. Enter h if my guess is bigger than yours. Otherwise enter l or h: ')
        if (user_input == 'c'):
            print('I dit it in', count, 'try')
            break
        if (user_input == 'l'):
            low_range = guess + 1
        if(user_input == 'h'):
            high_range = guess -1 
        

myGuess()
            

