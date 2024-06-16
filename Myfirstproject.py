# import first and last number 
# choose a randome number 
# ask for user choice 
# feedback to user 
# count down user choices 

import random 

user_firstnum= input ('please enter your first number'/n)
user_lastnum= input ('please enter your last number'/n)

count=5
if user_firstnum and user_lastnum == int:
 match_num= random.rand [user_firstnum, user_lastnum]
 while count >0:
 user_guess= input ('guess a number')
 if user_guess== match_num:
  print('win!')
 else:
  count-= 1
  input ('wrong make an other guess')
else:
 input ('please enter a valid number')
 print (count)

