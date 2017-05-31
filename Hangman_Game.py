from random_words import RandomWords

rw = RandomWords()
word = ''.join(rw.random_words())


def hangman():
    guesses = len(word)
    dashes = '-' * len(word)
    guessed = []

    while guesses > 0:
        print(dashes)
        guess = input('Enter a letter: ').lower()

        if guess in guessed:
            print("You've already guessed that letter")

        elif len(guess) > 1:
            print('You may only guess one letter at a time')

        elif not guess.isalpha():
            print('You may only guess letters')

        elif guess not in word:
            print(dashes + "You have %d guesses remaining" % guesses)
            print('Nope, that letter is not in the word')
            guessed.append(guess)
            guesses -= 1

        elif guess in word:
            guessed.append(guess)
            dashes = ''.join(j if j == guess else i for i, j in zip(dashes, word))
            print(dashes + "You have %d guesses remaining" % guesses)
            if '-' not in dashes:
                print("You Win")
                break

    return 'Game Over, the word was %s' % word


print(hangman())
