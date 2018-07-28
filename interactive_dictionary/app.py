# Interactive Dictionary Application

# Prompts Users repeatedly to Enter Words and then Defines them
# Suggests Most Similar Word to Misspelled Words

# Import Modules
from difflib import get_close_matches
import json



# Return Most Similar Word to Misspelled Word
# "dictionary" is a Python Dictionary that Contains a Mapping of Words to Definitions
def find_similar_word(dictionary, word):
    return get_close_matches(word, dictionary.keys())



# Define Word
# "dictionary" is a Python Dictionary that Contains a Mapping of Words to Definitions
def define(dictionary, word):

    # Lowercase All Words for Common Ground
    word = word.lower()

    # Lowercased Word Exists in Python Dictionary
    if word in dictionary:
        return dictionary[word]

    # Word is a Proper Name and Exists in Python Dictionary
    elif word.title() in dictionary:
        return dictionary[word.title()]

    # Word is an Acronym and Exists in Python Dictionary
    elif word.upper() in dictionary:
        return dictionary[word.upper()]

    # Word doesn't Exist in Python Dictionary
    # Find Most Similar Word
    elif len(find_similar_word(dictionary, word)) > 0:

        # Find Most Similar Word and Present to User
        similarWord = find_similar_word(dictionary, word)[0]
        response = input("Did you mean %s? Please enter 'yes' or 'no': " % (similarWord))

        # User Misspelled Word
        if response == "yes":
            return dictionary[similarWord]

        # User didn't Misspell Word
        elif response == "no":
            return "Sorry: The word doesn't exist in the dictionary. Please try another word."

        # User Gave an Invalid Response
        else:
            return "Sorry: Invalid Response"

    # User Gave an Invalid Word
    else:
        return "Sorry: The word doesn't exist in the dictionary. Please try another word."



# main() Function
# Load JSON Dictionary Data in a Python Dictionary
# Handle User Input
if __name__ == "__main__":

    # Load JSON Dictionary Data in a Python Dictionary
    file = open("data.json", "r")
    data = json.load(file)
    file.close()

    # Loop to Repeatedly Prompt Users for Words
    quit = False
    while (not quit):

        # Prompt User for a Word
        word = input("Please enter the word that you seek the definition of. Enter 'q' to quit: ")

        # Enable User to Quit Application at Any Time
        if word == 'q':
            quit = True

        if quit == False:

            # Define Word and Store Definition
            result = define(data, word)

            # Beautify Definition Output
            if type(result) == list:
                count = 1
                for definition in result:
                    print("Definition %s:" % (count), definition)
                    count += 1
                print("\n")

            else:
                print("Definition:", result)
                print("\n")
