# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"
def f():
    L = []
    inFile = open(WORDLIST_FILENAME, 'r')
    for x in inFile :
        if x != "\n" :
            L.append(x)
    inFile.close
    return L

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split(" ")
    print("  ", len(wordlist), "words loaded.")
    return wordlist
def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    counter =  0
    for i in secretWord :
        if i in lettersGuessed :
            counter += 1
    return counter == len(secretWord)
        



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guessedWord = "_ #"*len(secretWord)
    guessedWord = guessedWord.split("#")
    for i in range(len(secretWord)) :
        if secretWord[i] in lettersGuessed :
            guessedWord[i] =   secretWord[i]
    return "".join(guessedWord)
            



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    alphapet = list(string.ascii_lowercase)
    for i in lettersGuessed:
        if i in alphapet:
            alphapet.remove(i)
    return "".join(alphapet)

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is "+str(len(secretWord))+" letters long.")
    print("-------------")
    numberOfGuesses = 8
    lettersGuessed = []
    while numberOfGuesses >0 and isWordGuessed(secretWord, lettersGuessed) != True :
        print("You have "+str(numberOfGuesses)+" guesses left.")
        print("Available letters: "+getAvailableLetters(lettersGuessed))
        inputLetter = input("Please guess a letter: ").lower()
        if inputLetter in lettersGuessed :
            print("Oops! You've already guessed that letter: "+getGuessedWord(secretWord, lettersGuessed))
            print("-------------")
            continue
        else :
            lettersGuessed.append(inputLetter)
        if inputLetter in secretWord:
            print("Good guess: "+getGuessedWord(secretWord, lettersGuessed))
        else:
            numberOfGuesses -= 1
            print("Oops! That letter is not in my word: "+getGuessedWord(secretWord, lettersGuessed))
        print("-------------")

    if isWordGuessed(secretWord, lettersGuessed):
        print("Congratulations, you won!")
    else :
        print("Sorry, you ran out of guesses. The word was " + secretWord+".")
        
    