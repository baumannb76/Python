import random

comp_choice = random.choice(['rock', 'paper', 'scissors'])

user_choice = input('Do you want Rock, Paper or Scissors?')

if comp_choice == user_choice:
    print('TIE')
elif user_choice == 'rock' and comp_choice == 'scissors':
    print('WIN')
elif user_choice == 'paper' and comp_choice == 'rock':
    print('WIN')
elif user_choice == 'scissors' and comp_choice == 'paper':
    print('WIN')
else:
    print('You lose')
#print("The computer got " + comp_choice)