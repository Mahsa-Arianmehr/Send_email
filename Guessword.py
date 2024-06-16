# make a name list => choose a random name 
# show gaps for user => ask for guess
# put right guess in place => show error for wrong guess => count down guess numbers 


import random 

name_list = [ 'Mahsa', 'Bahar', 'Tara', 'Yekta', 'Kasra', 'Aria', 'Navid', 'Shayan']

r = random.choice (name_list).lower()
count=len (r)

gap_l = ['-'] * len(r)



while count > 0:
   user_guess=input ('enter your guess: \n')
   if user_guess.isalpha():
      if user_guess in r:
         if user_guess in gap_l:
            print('you guess it befor, try new')
         else:
            for idx, char in enumerate(r):
               if char== user_guess:
                  gap_l[idx]= user_guess
            current_guess= "-".join(gap_l)
            print(f'PERFECT=> {current_guess}')

            if not "-" in gap_l:
               print('you won')
               break

      else:
         print(f'wrong => remain gusses: {count}\n')
         count-=1
   else:
      print('please enter a valid alphabet \n') 
  
    
       
         
