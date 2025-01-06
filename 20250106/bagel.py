"""Bagels, 根据提示去猜一个随机数的值"""
import random

NUM_DIGITS = 3  # (!) Try setting this to 1 or 10.
MAX_GUESSES = 10  # (!) Try setting this to 1 or 100.


def main():
    print('''Bagels, a deductive logic game.
 I am thinking of a {}-digit number with no repeated digits.
 Try to guess what it is. Here are some clues:
 When I say: That means:
 Pico One digit is correct but in the wrong position.
 Fermi One digit is correct and in the right position.
 Bagels No digit is correct.

 For example, if the secret number was 248 and your guess was 843, the
 clues would be Fermi Pico.
 这是一个傻狗游戏，玩了会抑郁草'''.format(NUM_DIGITS))

    while True:
        secretNum = getSecretNum()
        print('I have thought up a number.')
        print(' You have {} guesses to get it.'.format(MAX_GUESSES))

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess #{}: '.format(numGuesses))
                guess = input('> ')

                clues = getClues(guess, secretNum)
                print(clues)
                numGuesses += 1
                if guess == secretNum:
                    break  # They're correct, so break out of this loop.

            if numGuesses > MAX_GUESSES:
                print('You ran out of guesses.')
                print('The answer was {}.'.format(secretNum))

                # Ask player if they want to play again.
                print('Do you want to play again? (yes or no)')
                if not input('> ').lower().startswith('n'):
                    break
                print('Thanks for playing!')


def getSecretNum():
    """Returns a string made up of NUM_DIGITS unique random digits."""
    numbers = list('0123456789')  # Create a list of digits 0 to 9.
    random.shuffle(numbers)  # Shuffle them into random order.

    # Get the first NUM_DIGITS digits in the list for the secret number:
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum


def getClues(guess, secretNum):
    """Returns a string with the pico, fermi, bagels clues for a guess
    and secret number pair."""
    if guess == secretNum:
        return 'You got it!'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')
        if len(clues) == 0:
            return 'Bagels'  # There are no correct digits at all.
        else:
            clues.sort()
    return ' '.join(clues)

# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()
