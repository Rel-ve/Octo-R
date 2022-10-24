import random

def game(comp,a): # Makes a function that compares the value provided by the computer and the player  
    if a == comp:
      print("Draw")
    elif a != comp:
        if ((comp == 's' and a == 'r') or (comp == 'p' and a == 's')):
            print("Player wins!") 
        elif ((comp == 'r' and a == 's') or (comp == 's' and a == 'p')):
            print("Computer wins!") 
        elif comp == 'r' and a == 'p':
            print("Player wins!")
        elif comp == 'p' and a == 'r':
            print("Computer wins!")

num = random.randint(1,3) # Picks a random number

if num == 1: # Converts num to r, p, s
    comp = 's'
elif num == 2:
    comp = 'r'
else:
    comp = 'p'

choice = input("Enter Scissors(s), Rock(r), Paper(p): ") 

if choice == 's' or choice == 'r' or choice == 'p': # Compares the values inputed by the user
   print("Choice of computer", comp)
   game(choice,comp)
else: # presents an error if the user has inputed any other characters outside of the specified string
   raise TypeError("Input valid option")
