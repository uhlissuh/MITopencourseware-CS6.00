# Problem Set 5: Ghost
# Name:
# Collaborators:
# Time:
#

import random

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print "  ", len(wordlist), "words loaded."
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq


# (end of helper code)
# -----------------------------------

# Actually load the dictionary of words and point to it with
# the wordlist variable so that it can be accessed from anywhere
# in the program.
wordlist = load_words()

def is_word(word, wordlist):
    for acceptableWord in wordlist:
        if word == acceptableWord:
            return True
    return False

def is_word_prefix(fragment, wordlist):
    for word in wordlist:
        if len(word) >= len(fragment):
            frag = ""
            for x in range(0, len(fragment)):
                frag += word[x]
            if fragment == frag:
                return True
    return False

def ghost():
    word_fragment = ""
    print "Welome to Ghost! Player 1 goes first."

    while True:
        for n in range(0, 2):
            current_player = "player " + str(n + 1)
            print "current word fragment:", word_fragment
            user_input = raw_input(current_player + " says letter:")
            user_letter = user_input.lower()
            word_fragment += user_letter
            if len(word_fragment) > 3 and is_word(word_fragment, wordlist) or not is_word_prefix(word_fragment, wordlist):
                print current_player + " loses."
                return


ghost()
