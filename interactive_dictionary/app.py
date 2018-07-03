from difflib import get_close_matches
import json

def find_similar_word(dictionary, word):
    return get_close_matches(word, dictionary.keys())

def define(dictionary, word):

    word = word.lower()

    if word in dictionary:
        return dictionary[word]

    elif word.title() in dictionary:
        return dictionary[word.title()]

    elif word.upper() in dictionary:
        return dictionary[word.upper()]

    elif len(find_similar_word(dictionary, word)) > 0:

        similarWord = find_similar_word(dictionary, word)[0]
        response = input("Did you mean %s? Please enter 'yes' or 'no': " % (similarWord))

        if response == "yes":
            return dictionary[similarWord]

        elif response == "no":
            return "Sorry: The word doesn't exist in the dictionary. Please try another word."

        else:
            return "Sorry: Invalid Response"

    else:
        return "Sorry: The word doesn't exist in the dictionary. Please try another word."

if __name__ == "__main__":

    file = open("data.json", "rb")
    data = json.load(file)
    file.close()

    word = input("Please enter the word that you seek the definition of: ")

    result = define(data, word)
    if type(result) == list:
        count = 1
        for definition in result:
            print("Definition %s:" % (count), definition)
            count += 1
    else:
        print("Definition:", result)
