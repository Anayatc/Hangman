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
        print(dashes)
        guess = input('Enter a letter: ').lower()
        if guess not in word:
            guesses -= 1
        while guesses > 0:
            return ''.join(['-' if guess != i else i for i in word_list])
    return 'Game Over'



print(hangman())