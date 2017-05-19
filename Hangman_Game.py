from random_words import RandomWords

rw = RandomWords()

# using the RandomWords Module selecting a random word and setting guesses to length of the random word
word = ''.join(rw.random_words())
# guesses = len(word)
print(word)


def hangman():
    guesses = len(word)
    word_list = [i for i in word]
    dashes = ['-' for i in word]
    guessed = []
    correct_guess = [i for i in guessed if i in word]
    while guesses > 0:
        print(''.join(dashes))
        guess = input('Enter a letter: ').lower()

        if guess in guessed:
            print("You've already guessed that letter")

        elif guess not in word:
            print(''.join(dashes))
            print('Nope, that letter is not in the word')
            guessed.append(guess)
            print('letters you have guessed: ' + str(guessed))
            guesses -= 1

        elif guess in word:
            guessed.append(guess)
            print('letters you have guessed: ' + guessed)
            dashes = ''.join(dashes.replace(dashes[word_list.index(guess)], guess))
            print(dashes)
            print('Yes, you have guessed a correct letter')

    return 'Game Over'


print(hangman())
