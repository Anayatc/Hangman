from random_words import RandomWords

rw = RandomWords()

# using the RandomWords Module selecting a random word and setting guesses to length of the random word
word = ''.join(rw.random_words())
# guesses = len(word)
print(word)


def hangman():
    guesses = len(word)
    word_list = [i for i in word]
    while guesses > 0:
        dashes = '-' * len(word)
        guess = input('Enter a letter: ').lower()
        guessed = []
        if guess not in word:
            print(dashes)
            guessed.append(guess)
            guesses -= 1
        elif guess in word:
            guessed.append(guess)
            dashes = ''.join(['-' if guess != i and guess not in guessed else i for i in word_list])
            print(dashes)
    return 'Game Over'

print(hangman())
