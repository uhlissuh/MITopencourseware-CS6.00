import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

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


def get_word_score(word, n):

    wordTotal = 0
    for letter in word:
        wordTotal += SCRABBLE_LETTER_VALUES[letter]
    if len(word) == n:
        wordTotal += 50

    return wordTotal



def display_hand(hand):

    for letter in hand.keys():
        for j in range(hand[letter]):
            print letter,              # print all on the same line
    print                              # print an empty line

def deal_hand(n):

    hand={}
    num_vowels = n / 3

    for i in range(num_vowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1

    for i in range(num_vowels, n):
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1

    return hand



def update_hand(hand, word):
    updatedHand = hand.copy()
    for key in hand:
        for letter in word:
            if key == letter:
                updatedHand[key] = updatedHand[key] - 1
        if updatedHand[key] <= 0:
            del updatedHand[key]
    return updatedHand


def is_valid_word(word, hand, word_list):
    handCopy = hand.copy()

    for letter in word:
        if handCopy.get(letter, 0) == 0:
            return False
        else:
            handCopy[letter] -= 1

    for acceptableWord in word_list:
        if acceptableWord == word:
            return True

    return False


# # Problem #4: Playing a hand
# #
def play_hand(hand, word_list):
    handTotal = 0

    while True:
        display_hand(hand)
        user_input = raw_input("Enter word, or a . to indicate that you are finished:")
        if user_input == ".":
            print "Total score:", handTotal, "points"
            return

        while not is_valid_word(user_input, hand, word_list):
            user_input = raw_input("word invalid, enter new:")
            if user_input == ".":
                print "Total score:", handTotal, "points"
                return

        wordTotal = get_word_score(user_input, 7)
        handTotal += wordTotal
        print user_input, "earned", wordTotal,  "points. Total:", handTotal, "points"
        hand = update_hand(hand, user_input)



# Problem #5: Playing a game

def play_game(word_list):
    hand = deal_hand(HAND_SIZE)

    while True:
        cmd = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if cmd == 'n':
            hand = deal_hand(HAND_SIZE)
            play_hand(hand.copy(), word_list)
            print
        elif cmd == 'r':
            play_hand(hand.copy(), word_list)
            print
        elif cmd == 'e':
            break
        else:
            print "Invalid command."


#Build data structures used for entire session and play game

if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
