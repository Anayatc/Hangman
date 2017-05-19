from random_words import RandomWords

rw = RandomWords()

# using the RandomWords Module selecting a random word and setting guesses to length of the random word
word = ''.join(rw.random_words())
# guesses = len(word)
print(word)


def hangman():
    guesses = len(word)
    word_list = [i for i in word]
    dashes = '-' * len(word)
    guessed = []
    letters_in_word_list = list(set(word_list))
    print(letters_in_word_list)
    while guesses > 0:
        print(''.join(dashes))
        guess = input('Enter a letter: ').lower()

        if guess in guessed:
            print("You've already guessed that letter")

        elif len(guess) > 1:
            print('You may only guess one letter at a time')

        elif not guess.isalpha():
            print('You may only guess letters')

        elif guess not in word:
            print(''.join(dashes))
            print('Nope, that letter is not in the word')
            guessed.append(guess)
            print('Letters you have guessed: ' + str(guessed.sort()))
            guesses -= 1

        elif guess in word:
            guessed.append(guess)
            print('Letters you have guessed: ' + str(guessed.sort()))
            dashes = dashes.replace(dashes[word.index(guess)], guess)
            print(dashes)
            print('Yes, you have guessed a correct letter')

        elif len(''.join(guesses)) == word and letters_in_word_list.sort() == guessed.sort():
            print('You Win')

    return 'Game Over'


print(hangman())
