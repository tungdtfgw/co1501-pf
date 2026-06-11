import random as rd

n = rd.randint(1, 100)

incorrect = True

while incorrect:
    number = int(input('Guess a number between 1 and 10: '))
    print(f'You guessed: {number}')
    if number == n:
        print('Correct!')
        incorrect = False
    elif number < n:
        print('Too low, try again.')
    else:
        print('Too high, try again.')