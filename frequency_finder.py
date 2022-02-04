'''
Combing through the list of five letter words each time to figure out what
the frequencies are for each letter at each position would be an inefficient approach.
This program accomplishes that goal, then stores the data into a json file.

It should only be neccessary to run this program once
'''
import json
import pprint
from string import ascii_lowercase as alphabet


def grab_words_from_file():
    words = []
    with open("five-letter-words.txt", "r") as file:
        for word in file.readlines():
            # Words are already in lowercase but just to be cautious...
            words.append(word.lower())
    return words

def position_letter_count_4_one_word(word):
    return {(i+1):word[i] for i in range(5)}

def empty_letter_and_positions_dict():
    empty_positions_dict = {letter:0 for letter in alphabet}

    counts_at_a_position = {
        1: empty_positions_dict.copy(),
        2: empty_positions_dict.copy(),
        3: empty_positions_dict.copy(),
        4: empty_positions_dict.copy(),
        5: empty_positions_dict.copy()
    }
    return counts_at_a_position

def position_letter_count_4_all_words(words):
    counts_at_5_positions = empty_letter_and_positions_dict()    

    for word in words:
        letter_positions = position_letter_count_4_one_word(word)
        for position, letter in letter_positions.items():
            counts_at_5_positions[position][letter] += 1
    
    return counts_at_5_positions

def letter_counts_2_frequencies_4_all_words(letter_counts_at_positions, num_of_words):
    for position in letter_counts_at_positions:
        for letter in alphabet:
            letter_counts_at_positions[position][letter] /= num_of_words
    return letter_counts_at_positions

def save2json(data_dict, path):
    with open(path, "w", encoding='utf-8') as file:
        json.dump(data_dict, file, ensure_ascii=True, indent=4)


if __name__ == "__main__":
    words = grab_words_from_file()
    letter_counts = position_letter_count_4_all_words(words)
    frequency_counts = letter_counts_2_frequencies_4_all_words(letter_counts, len(words))

    letter_frequencies_file = "letter_frequency.json"
    save2json(frequency_counts, letter_frequencies_file)
