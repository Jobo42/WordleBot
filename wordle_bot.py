'''
Code by Liam Hade. Algorithm by Mickey Claffey.
'''
import json
from frequency_finder import grab_words_from_file


def grab_frequencies_from_file(path):
    with open(path, "r") as file:
        return json.load(file)

def best_first_word(words, position_letter_frequencies):
    for po

class WordleBot:
    def __init__(self):
        self.used_words = []
    
    def best_word_guess(self):
        pass


letter_frequencies_file = "letter_frequency.json"
words = grab_words_from_file()
letters = grab_frequencies_from_file(letter_frequencies_file)
print(letters)