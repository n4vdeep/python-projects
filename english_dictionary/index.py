import json
import difflib

from difflib import  SequenceMatcher, get_close_matches

data = json.load(open("data.json"))
# print(data.keys())

message = "Unrecognized Word"

def meaning_of(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data: #if user entered "texas" this will check for "Texas" as well.
        return data[word.title()]
    elif word.upper() in data: #if user entered "usa" this will check for "USA" as well.
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        confirmation_msg = input(f"Did you mean '{get_close_matches(word, data.keys())[0]}'? Enter Y if Yes, N if No: ")
        if confirmation_msg == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif confirmation_msg == "N":
            return 'That word does not exist. Please double check it'
        else:
            return "Sorry that response is not recognised"
    else:
        return f"{message}"

word = input("Enter a word: ")

output = meaning_of(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)