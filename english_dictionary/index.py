import json
import difflib

from difflib import  SequenceMatcher

def meaning_of(word):
    data = json.load(open("data.json"))
    message = "Unrecognized Word"
    try:
        return data[word]
    except KeyError:
        return f"{message}"

word = input("Enter a word: ").lower()

print(meaning_of(word))