import json

file = open("data.json", "rb")
data = json.load(file)

def definition(word):
    return data[word]

if __name__ == "__main__":
    word = input("Please enter the word that you seek the definition of: ")
    print(definition(word))
