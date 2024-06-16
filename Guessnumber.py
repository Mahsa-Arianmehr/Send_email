# user input => low and hight bound *
# random number [a,b] *
# loop => condition => guess count= 5 => feedback

import random
try:
    low = int(input('Enter lower bound: \n')) 
    high = int(input('Enter higher bound: \n'))
except:
    print('please enter valid number')
r= random.randint(low, high)

guess_count=5

while guess_count>0:
    try:
         new_guess_str= input(f'remain guess: {guess_count} => enter your next guess: \n')
         new_guess= int(new_guess_str)

         if r== new_guess:
          print('great, your guess is correct')
          break
         elif r>new_guess:
          print(' your guess is lower than selected number')
         else:
          print(' your guess is higher than selected number')
         guess_count -= 1
    except:
         print('please enter valid number')

    
    
        

       













