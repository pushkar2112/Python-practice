# The Challenge:

# Write a program that picks a random integer from 1 to 100, and has players guess the number.
 
# The rules are:

# If a player's guess is less than 1 or greater than 100, say "OUT OF BOUNDS"
# On a player's first turn, if their guess is
#   within 10 of the number, return "WARM!"
#   further than 10 away from the number, return "COLD!"
# On all subsequent turns, if a guess is
#   closer to the number than the previous guess return "WARMER!"
#   farther from the number than the previous guess, return "COLDER!"
# When the player's guess equals the number, tell them they've guessed correctly and how many guesses it took!

import random

def limcheck():
    global guess_count, guess_check
    while True:
        try:
            guess = int(input('Take a guess...\n'))
        except ValueError:
            print("oops! That wasn't a number!")
            continue
        if guess < 1 or guess > 100:
            print('OUT OF BOUNDS')
            print('Take another guess')

            guess_count -= 1
        else:
            guess_count -= 1
            guess_check += 1
            guess_list.append(guess)
            return guess
            break

secret_number = random.randint(1, 100) # Number to be guessed by the user
guess_count = 10 # guess counter to run the while loop
guess = None
ch = None
guess_list = []  # list to store user guesses
guess_check = 0  # Number of guesses taken

#--------RULES-------------
print('WELCOME TO THE GUESSING GAME!!!')
print('The rules are as follows: ')
print("""
1.Player's guess should be between 1 and 100 (Including 1 and 100). 
2.On a player's first turn, if their guess is
  > within 10 of the number, game returns "WARM!"
  > further than 10 away from the number, game returns "COLD!"
3.On all subsequent turns, if a guess is
  > closer to the number than the previous guess, game returns "WARMER!"
  > farther from the number than the previous guess, game returns "COLDER!"
4.A player has a total of 10 guesses to guess the number
5.Game messages:
  > "OUT OF BOUNDS" - Guess made outside the range
  > "SUCCESS" - Correct guess
  > "GAME OVER" - Out of moves""")

print(secret_number)
ch = input('Press Enter to start the game...')

#------------GAME LOGIC-------------
while guess_count > 0:
    guess = limcheck()
    if guess == secret_number:
        print('SUCCESS')
        print('You have guessed correctly.')
        print(f'You have used {guess_check} guesses.')
        break
    if guess_check == 1:    
        if abs(secret_number-guess) <= 10:
            print('WARM!')
        else:
            print('COLD!')
    elif guess_check > 1:
        if abs(secret_number-guess) < abs(secret_number-guess_list[-2]):
            print('WARMER!')
            continue
        else:
            print('COLDER!')
            continue
    elif guess_check >10:
        print('GAME OVER')
        print('You have exhausted all your guesses!!!')
        print(f'The number was {secret_number}')
        print('BETTER LUCK NEXT TIME')
        break


