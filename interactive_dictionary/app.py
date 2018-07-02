import json

def definition(dictionary, word):

    word = word.lower()

    if word in dictionary:
        return dictionary[word]
    else:
        return "Sorry: The word doesn't exist in the dictionary. Please try another word."

if __name__ == "__main__":

    file = open("data.json", "rb")
    data = json.load(file)

    word = input("Please enter the word that you seek the definition of: ")
    print(definition(data, word))
