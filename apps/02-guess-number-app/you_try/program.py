import random

print('-------------------------------------')
print('       GUESS THAT NUMBER GAME        ')
print('-------------------------------------')
print()

player_name = input('Please enter your name: ')
the_number = random.randint(0, 100)
guess = ''
try_count = 10

print('Hello {}, welcome the the number game. You have ten chances to guess a random number between 0 and 100\
. Good luck!'.format(player_name))

while True:
    guess_text  = input('Guess a number: ')
    guess = int(guess_text)
    if guess < the_number and try_count > 1:
        try_count -= 1
        print('Sorry {} is LOWER than the number. \n{} tries left..'.format(guess, try_count))
    elif guess > the_number and try_count > 1:
        try_count -= 1
        print('Sorry {} is HIGHER than the number. \n{} tries left..'.format(guess, try_count))
    elif guess == the_number and try_count > 1:
        print('Congratulations {}! You\'ve guessed the correct number with {}'.format(player_name, the_number))
        break
    else:
        print('Sorry {}, you\'ve ran out of guesses. :( Maybe next time!')
        break 