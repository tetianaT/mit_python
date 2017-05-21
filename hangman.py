# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
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
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    if set(secret_word).issubset(set(letters_guessed)):
       return True
    else:
        return False

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    guessed = "_ " * len(secret_word)
    guessed = guessed.split(" ")
    for i in letters_guessed:
        for j in range(len(secret_word)):
            if i == secret_word[j]:
                guessed[j] = i
    return (" ").join(guessed)


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    whats_left = string.ascii_lowercase
    for i in letters_guessed:
        if i in whats_left:
            whats_left = whats_left.replace(i, "")
    return whats_left


def duplicate(my_list, letter):
    """
    checks if the user already entered a letter 
    """
    if letter in my_list[0:-1] and len(my_list) > 1:
        return True
    else:
        return False


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    print "Welcome to the game Hangman!"
    print "I'm thinking of the word that is", len(secret_word), "letters long."
    print "-" * 15 + "\n"
    print "You have 3 warnings left"
    secret_word = secret_word.lower()
    guess = 6
    warning = 3
    vowels = "aeiou"
    letters_guessed = []
    while guess > 0:
        gues = get_guessed_word(secret_word, letters_guessed)
        print "You have", guess, "guesses left."
        print "Available letters:",(get_available_letters(letters_guessed))
        print "Please, guess a letter: "
        letter = raw_input().lower()
        if letter.isalpha() and len(letter) == 1:
            letters_guessed.append(letter)
            if get_guessed_word(secret_word, letters_guessed) != gues:
                print "Good guess!"
            elif get_guessed_word(secret_word, letters_guessed) == gues:
                if duplicate(letters_guessed, letter) == True:
                    if warning > 0:
                        warning -= 1
                        print "Oops! You already guessed that letter! You have", warning, "warnings left."
                    else:
                        guess -= 1
                        print "Oops! You already guessed that letter!"
                        print "You have no warnings left! So you lose 1 guess"
                        print "The number of guesses is:", guess
                else:
                    if letter and not letter in vowels:
                        guess -= 1
                        print "Oops! That is not a letter I have in my word. You have", guess, "guesses left."
                    elif letter.isalpha() and letter in vowels:
                        guess -= 2
                        print "Oops! That is not a letter I have in my word. You have", guess, "guesses left."
            print get_guessed_word(secret_word, letters_guessed)
            print "-" * 15 + "\n"
        else:
            if warning > 0:
                warning -= 1
                print "Oops! That is not a valid letter! You have", warning, "warnings left!"
            else:
                guess -= 1
                print "Oops! That is not a valid letter!"
                print "You have no warnings left! So you lose 1 guess"
                print "The number of guesses is:", guess
        if is_word_guessed(secret_word, letters_guessed):
            print "Congratulations! Your score is:", guess * len(set(secret_word))
            break
    if guess == 0:
        print "Sorry, you ran out of guesses! The word was", secret_word




def match_with_gaps(my_word, other_word, available_letters):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    my_word = "".join(my_word.split(" "))
    other_word = other_word.strip()
    if len(my_word) == len(other_word):
        for i in range(len(my_word)):
            if my_word[i] != "_":
                if my_word[i] != other_word[i]:
                    return False
                    break
            elif not other_word[i] in available_letters:
                return False
                break
        w1 = {i: my_word.count(i) for i in set(my_word)}
        w2 = {i: other_word.count(i) for i in set(other_word)}
        for k in w1:
            if k != "_":
                if w1[k] != w2[k]:
                    return False
                    break
    else:
        return False
    return True


def show_possible_matches(my_word, available_letters):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    my_list = []
    for word in wordlist:
        if match_with_gaps(my_word, word, available_letters):
            my_list.append(word)
    if my_list:
        print "Possible word matches are:"
        return " ".join(my_list)
    else:
        print "No matches found!"


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word.

    * If the letter was guessed and not included in the word,
      possible matches won't show such words

    * If there's only one mathching word left, after user
      asks for the hint - print the winning message
    
    Follows the other limitations detailed in the problem write-up.
    '''
    print "Welcome to the game Hangman!"
    print "I'm thinking of the word that is", len(secret_word), "letters long."
    print "-" * 15 + "\n"
    print "You have 3 warnings left"
    secret_word = secret_word.lower()
    guess = 6
    warning = 3
    vowels = "aeiou"
    letters_guessed = []
    while guess > 0:
        matches = show_possible_matches(get_guessed_word(secret_word, letters_guessed),
                                        get_available_letters(letters_guessed))
        gues = get_guessed_word(secret_word, letters_guessed)
        print "Available letters:", (get_available_letters(letters_guessed))
        print "Please, guess a letter: "
        letter = raw_input().lower()
        if letter == "*":
            print matches
            print "length of matches", len(matches)
            if len(matches.split(" ")) == 1:
                print "You have 1 possible match left. You won! Your score is:", guess * len(set(secret_word))
                break
        elif not letter.isalpha() and not letter == "*" or not len(letter) == 1:
            if warning > 0:
                warning -= 1
                print "Oops! That is not a valid letter! You have", warning, "warnings left!"
            else:
                guess -= 1
                print "Oops! That is not a valid letter!"
                print "You have no warnings left! So you lose 1 guess"
                print "The number of guesses is:", guess
        else:
            letters_guessed.append(letter)
            if get_guessed_word(secret_word, letters_guessed) != gues:
                print "Good guess!"
            elif get_guessed_word(secret_word, letters_guessed) == gues:
                if duplicate(letters_guessed, letter) == True:
                    if warning > 0:
                        warning -= 1
                        print "Oops! You already guessed that letter! You have", warning, "warnings left."
                    else:
                        guess -= 1
                        print "Oops! You already guessed that letter!"
                        print "You have no warnings left! So you lose 1 guess"
                        print "The number of guesses is:", guess
                else:
                    if letter and not letter in vowels:
                        guess -= 1
                        print "Oops! That is not a letter I have in my word. You have", guess, "guesses left."
                    elif letter.isalpha() and letter in vowels:
                        guess -= 2
                        print "Oops! That is not a letter I have in my word. You have", guess, "guesses left."
            print get_guessed_word(secret_word, letters_guessed)
            print "-" * 15 + "\n"

        if is_word_guessed(secret_word, letters_guessed):
            print "Congratulations! Your score is:", guess * len(set(secret_word))
            break
    if guess == 0:
        print "Sorry, you ran out of guesses! The word was", secret_word


if __name__ == "__main__":
    secret_word = choose_word(wordlist)
    #print hangman_with_hints(secret_word)
    print hangman(secret_word)

