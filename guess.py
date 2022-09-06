# GUESS GAME
import random
import sys 


guess_count = 0

number = random.randint(1, 10)

allowed_guess_count = 6


print("Try to guess a number between 1 and 10 in 6 tries. Let's GO")


# make a loop for player to try 'n' number of times
for guesses in range(1, allowed_guess_count + 1):   
    # handle exception if player returns an invalid input or character
    
    try:    
        guess = int(input('Guess a number between 1 and 10:'))
    except Exception:
        print('Invalid Input. Only integers are allowed')
    else:
        if number > guess:
            print('Oops, your guess is less than the answer')
        elif number < guess:
            print('Oops, your  guess is greater than the answer')
        else:
            print(f'Hurray, your guess is correct. You guessed the number in {guesses} try' if guesses == 1 else f'Hurray, your guess is correct. You guessed the number in {guesses} tries')
            sys.exit()

        print('')

        tries_left = allowed_guess_count - guesses
        
        if number == guess:
            pass
        else:
            print(f'You have {tries_left} trie(s) left!') # Assign no. of tries left if guess isn't correct

    if guesses == 6 and number != guess:
        print('.......')
        print('Game over. You tried to guess the number and failed. LOOSER')
    elif guesses == 6 and number == guess:
        print('........')
        print('Hurray, your guess is correct. You are so lucky, got it at last try')



