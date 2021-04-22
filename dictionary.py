import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0 :
        yn = input("Do you mean %s ? Enter Y for yes and N for no." % get_close_matches(word, data.keys()) [0])
        if yn == "y":
            return data[get_close_matches(word, data.keys()) [0]]
        elif yn == "n":
            return  "Sorry the word you entered does not exist"
        else:
            return "Sorry we do not understand your input"
    else:
        return "Sorry the word you entered does not exist"

word = input("Enter word: ")

output = translate(word)

if type(output) == list:
    for i in output:
        print(i)
else:
    print(output)
