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
    while guesses > 0:
        guess = input('Enter a letter: ').lower()
        if guess in guessed:
            print("You've already guessed that letter")
        elif guess not in word:
            print(dashes)
            print('Nope, that letter is not in the word')
            guessed.append(guess)
            print(guessed)
            guesses -= 1
        elif guess in word:
            guessed.append(guess)
            print(guessed)
            dashes = ''.join(['-' if guess != i and guess in guessed else i for i in word_list])
            print(dashes)
    return 'Game Over'

print(hangman())
