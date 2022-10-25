import random 
import os.path

CompGuess = random.randint(1,10)
i = False
guesses = 0
while i != True:
    UserGuess = int(input("Enter your number: "))
    if UserGuess == CompGuess:
        guesses += 1
        break
    elif UserGuess > CompGuess:
        print("Guess lower")
        guesses += 1

    elif UserGuess < CompGuess:
        print("Guess higher")
        guesses += 1

print(f"You guessed the number {CompGuess} in {guesses} tries!")

if not(os.path.exists('HighScore.txt')):
    with open("HighScore.txt", "w") as f:
          f.write(str(guesses))

else:
    with open("HighScore.txt", "r") as f:
        highscore = int(f.read())
    
    if guesses < highscore:
        with open ("HighScore.txt", "w") as f:
            f.write(str(guesses))
            
        print("You just beat the high score!")
  
    else:
        print(f"Try again, your highest score is {highscore}")
