import random

def get_random_secret():
    secret = random.randint(0, 100)
    print("The number is between 0 and 100")
    return secret

def is_guess_valid(the_guess):
    return the_guess >= 0 and the_guess <= 100

def how_off_is_the_guess(the_guess, the_secret):
    diff = abs(the_guess - the_secret)
    if diff < 5:
        print('Very hot!')
    elif diff > 5 and diff <= 10:
        print('A little bit hot')
    elif diff > 10 and diff <= 15:
        print("It's a little bit cold here!")
    else:
        print('Very cold like Antarctica')

the_secret = get_random_secret()
counter = 1
try:
    while True:
        the_guess = int(input('Please give a number: '))

        if is_guess_valid(the_guess): 
            if the_guess == the_secret:
                print(f'Congrats! The secret was {the_secret}. You found the secret after {counter} attempts.')
                break
            else:
                how_off_is_the_guess(the_guess, the_secret)
            counter += 1
        else: 
            print('Please enter a valid number in the range [0, 100]')
except ValueError:
    print("Please enter a valid input")