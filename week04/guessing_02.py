import random as rd

n = int(input('Enter a number between 1 and 100: '))

incorrect = True
low = 1
high = 100

while incorrect:
    guess = (low + high) // 2
    print(f'Computer guesses: {guess}')
    if guess == n:
        incorrect = False
        print('Correct!')
    elif guess < n:
        print('Too low, trying again.')
        low = guess + 1
    else:
        print('Too high, trying again.')
        high = guess - 1