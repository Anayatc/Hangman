# Hangman

## Project Description:
A Hangman game, that selects a random word from a dictionary, the user is allowed a number of guesses equivalent to the length of the word. 

## Project Objective:
Initially intended on either creating a list of words and returning one item from the list at random. Or html scrapping a word from dictionary.com, but settled on using the RandomWord module as it has a huge list of words and can return a word at random and does not contain names or proper nouns.  
I set the number of allowed guesses to the length of the word. I aslo wanted a visual representation of the words as hyphons, e.g. 'apple' would be printed out as '-----' a correct guess would then replace the hyphon with the letter that has been guessed correctly. Therefore guessing a would print 'a----' for the next turn and so on until either the number of guesses reaches maximum and the game is over or the word is guessed correctly. This proved the most difficult part to implement (and currently is not working)


## Stack Elements:
1. Python 3.6 
2. imports: RandomWords - returns a random word from a large dictionary
  

## How to Run:
1. install python 3.6, or any python 3 version
2. pip or easy install RandomWord - `pip install RandomWord`
3. clone reopository
4. cd to location of cloned repository
5. run in python shell

## Testing:
I have not unit tested this code as it is in essence a very simple program, that takes user inputs, therefore testing for user inputs would be somewhat complex meaning testing the program would be substanially more time intentsive than a program of this nature is worth. 

## Bugs:
1. the print statement after correct guess isn't working as expected.
2. after guessing the word correctly it still allows user to inout guesses.
3. ~~inputting a guess that has already been made doesn't return an error.~~
