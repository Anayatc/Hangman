from random_words import RandomWords

rw = RandomWords()

# using the RandomWords Module selecting a random word and setting guesses to length of the random word
word = ''.join(rw.random_words())
# guesses = len(word)
print(word)


def hangman():
    guesses = len(word)
    while guesses > 0:
        dashes = '-' * len(word)
        print(dashes)
        guess = input('Enter a letter: ').lower()
        if guess not in word:
            guesses -= 1
        elif guess in word:
            return [i for i in word]
    return 'Game Over'



print(hangman())