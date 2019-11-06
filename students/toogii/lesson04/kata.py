#!/usr/bin/env python3
from copy import copy
import random


clean_up_dict = {".": "", ",": "", "\"": "", "\'": "", "(": "", ")": "", "-": " "}


def build_the_sentence(trigram_dict):
    # This function builds sentence from the passted trigram starting from the random index
    random_index = random.randint(0, len(list(clean_and_create_trigram(file, clean_up_dict)))-1)
    print("\nStarting from {}\n" .format(random_index+1))
    key_list = list(trigram_dict.keys())[random_index:]
    value_list = list(trigram_dict.values())[random_index:]
    sentence_list = list(key_list[0])
    for i in range(0, len(key_list)-1):
        if (key_list[i][1], value_list[i][0]) == key_list[i+1]:
            sentence_list.extend(value_list[i])
            continue
        sentence_list.extend(list(key_list[i+1]))
        sentence_list.extend(value_list[i])
    sentence_list.append(list(trigram_dict.values())[-1][0])

    print("\n\nPrinting the sentence starting from {}\n\n" .format(random_index+1))
    print(" ".join(sentence_list))


def clean_and_create_trigram(file: str, clean_up_dict: dict) -> dict:
    # This function cleans up the passed file and created trigram dictionary from it.
    line_trailer = tuple()
    trigram_dict = dict()
    with open(file) as f:
        for line in f:
            if '***' in line:
                continue
            clean_line = line.translate(line.maketrans(clean_up_dict)).strip().split(" ")
            clean_line_copy = copy(clean_line)
            for word in clean_line_copy:
                if word == '':
                    clean_line.remove(word)
            if line_trailer:
                clean_line.insert(0,line_trailer[0])
                clean_line.insert(1,line_trailer[1])
            for index in range(len(clean_line)-2):
                trigram_dict[tuple(clean_line[index:index+2])] = trigram_dict.get(tuple(clean_line[index:index+2]), []) + [clean_line[index+2]]
                line_trailer = (clean_line[index+1],clean_line[index+2])
    return trigram_dict


if __name__ == '__main__':
    file = str(input("Please enter the filename including path: "))
    trigram_dict = clean_and_create_trigram(file, clean_up_dict)
    print("\n\nPrinting the trigram dictionary created from {}\n\n".format(file))

    print(trigram_dict)
    build_the_sentence(trigram_dict)
