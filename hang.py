# -*- coding: utf-8 -*-

import random
import string
import logging
import sys

WORDLIST_FILENAME = "palavras.txt"

def logSys(log, message):
    logger = logging.getLogger('Logger Message')
    logger.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s -%(name)s - %(levelname)s - %(message)s ')

    ch.setFormatter(formatter)

    logger.addHandler(ch)

    if log == 'debug':
        logger.debug(message)

    elif log == 'info':
        logger.info(message)

    elif log == 'warnning':
        logger.warn(message)

    else:
        logger.error(message)

def validSecretWord(secretWord):
    if secretWord.__class__ is not str:
        logSys('debug','Secret Word não é uma string')
        sys.exit()

#Function that draws the gallows and doll according to the number of errors.
class Hangman():
    def hangman_man(self, guesses):

        if guesses == 8:
			print "________      "
			print "|             "
			print "|             "
			print "|             "
			print "|             "
			print "|             "
        elif guesses == 7:
            print "________      "
            print "|      |      "
            print "|             "
            print "|             "
            print "|             "
            print "|             "
        elif guesses == 6:
            print "________      "
            print "|      |      "
            print "|      ~      "
            print "|             "
            print "|             "
            print "|             "
        elif guesses == 5:
            print "________      "
            print "|      |      "
            print "|      õ      "
            print "|             "
            print "|             "
            print "|             "
        elif guesses == 4:
            print "________      "
            print "|      |      "
            print "|      õ      "
            print "|      |      "
            print "|             "
            print "|             "
        elif guesses == 3:
            print "________      "
            print "|      |      "
            print "|      õ      "
            print "|     /|      "
            print "|             "
            print "|             "
        elif guesses == 2:
            print "________      "
            print "|      |      "
            print "|      õ      "
            print "|     /|\     "
            print "|             "
            print "|             "
        elif guesses == 1:
            print "________      "
            print "|      |      "
            print "|      õ      "
            print "|     /|\     "
            print "|     /       "
            print "|             "
        else:
            print "________      "
            print "|      |      "
            print "|     \õ/     "
            print "|      |      "
            print "|     / \     "
            print "|             "


def loadWords():
    """
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'read', 0)
    logSys('info','Arquivo aberto com sucesso!')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return random.choice(wordlist)


def isWordGuessed(secretWord, letters_guessed):
    secret_Letters = []

    for letter in secretWord:
        if letter in letters_guessed:
            pass
        else:
            return False

    return True

def get_available_letters():
    import string
    # 'abcdefghijklmnopqrstuvwxyz'
    available = string.ascii_lowercase

    return available

# This function counts how many letters the word has and warn you how many different letters there are in the word.
def count_letters(secretWord):

    letters = []

    for letter in secretWord:
        if letter not in letters:
            letters.append(letter)

    return len(letters)

# This function validates if the word has different letters have the same size as the attempts.
def validated_word (secretWord, guesses):
    MAXIMUM_TRIES = 20
    tries = 0
    validated_word = False

    while not validated_word:
        unique_letters = count_letters(secretWord)
        print 'There are', unique_letters, 'unique Letters in this word'

        if guesses < unique_letters:
            logSys('info','The secret Word have too many unique letters, reloading the letters, reloading')
            secretWord = loadWords()
            tries += 1
            if tries >= MAXIMUM_TRIES:
                logSys('error','Max of tries, exiting program')
                return None
        else:
            validated_word = True
    return secretWord

def guessed_letters(secretWord, letters_guessed):
    guessed = ''
    for letter in secretWord:
        if letter in letters_guessed:
            guessed += letter
        else:
            guessed += '_ '

    return guessed

def show_available_letters(letters_guessed):
    available = get_available_letters()
    for letter in available:
        if letter in letters_guessed:
            available = available.replace(letter, '')
    print 'Available letters', available

def hangman(secretWord):
    guesses = 8
    secretWord = validated_word(secretWord, guesses)

    if secretWord == None:
        return ''

    letters_guessed = []

    hangman = Hangman()

    print 'Welcome to the game, Hangam!'
    print 'I am thinking of a word that is', len(secretWord), ' letters long.'
    print '-------------'

    while  isWordGuessed(secretWord, letters_guessed) == False and guesses >= 0:
        print 'You have ', guesses, 'guesses left.'

        hangman.hangman_man(guesses)

        if guesses == 0:
            return

        show_available_letters(letters_guessed)

        letter = raw_input('Please guess a letter: ')

        if letter.isdigit():
            logSys('error','Not a letter')

        if letter in letters_guessed:
            guessed = ''
            guessed = guessed_letters(secretWord, letters_guessed)

            print 'Oops! You have already guessed that letter: ', guessed
        elif letter in secretWord:
            letters_guessed.append(letter)

            guessed = ''
            guessed = guessed_letters(secretWord, letters_guessed)

            print 'Good Guess: ', guessed
        else:
            guesses -=1
            letters_guessed.append(letter)

            guessed = ''
            guessed = guessed_letters(secretWord, letters_guessed)

            logSys('warnning', 'Oops! That letter is not in my word')
            print guessed
        print '------------'

    else:
        if isWordGuessed(secretWord, letters_guessed) == True:
            print 'Congratulations, you won!'
        else:
            print 'Sorry, you ran out of guesses. The word was ', secretWord, '.'

secretWord = loadWords().lower()
hangman(secretWord)
