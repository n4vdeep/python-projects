import json
import difflib

from difflib import  SequenceMatcher, get_close_matches

data = json.load(open("data.json"))
# print(data.keys())

message = "Unrecognized Word"

def meaning_of(word):
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        confirmation_msg = input(f"Did you mean '{get_close_matches(word, data.keys())[0]}'? Enter Y if Yes, N if No: ")
        if confirmation_msg == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif confirmation_msg == "N":
            pass
        else:
            print ("Sorry that response is not recognised, Please respond with Y (Yes) or N (No)")
            confirmation_msg = input(f"Did you mean '{get_close_matches(word, data.keys())[0]}'? Enter Y if Yes, N if No: ")
    else:
        return f"{message}"

word = input("Enter a word: ").lower()

print(meaning_of(word))