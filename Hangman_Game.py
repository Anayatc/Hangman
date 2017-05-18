from random_words import RandomWords
rw = RandomWords()

word = ''.join(rw.random_words())
guesses = len(word)
print(word, guesses)

def hangman():
    pass