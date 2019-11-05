import random
guessesLeft = 7

number = random.randint(1, 100)
print('I am the Riddler and I have a riddle for you. I am thinking of a number between 1 to 100 and I'll give you 7 tries to guess it.')

while guessesLeft > 0:
    print('What is your guess?')
    guess = input()
    guess = int(guess)

    guessesLeft = guessesLeft - 1

    if guess < number:
        print('Your guess is too high!') 
    if guess > number:
        print('Your guess is too low!')

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print('Ah, you are a smart one. You guessed my number with ' + guessesLeft + ' tries left!')

if guess != number:
    number = str(number)
    print('Out of tries! The number I was thinking of was ' + number + '. Better luck next time!')
