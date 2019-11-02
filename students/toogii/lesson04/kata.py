#!/usr/bin/env python3


clean_up_dict = {".": "", ",": "", "\"": "", "\'": ""}
trigram_dict = dict()
spaceless_clean_line = list()


def clean_and_create_trigram(file, clean_up_dict: dict):
    with open(file) as f:
        for line in f:
            if line[:3] == "***":
                continue
            clean_line = line.translate(line.maketrans(clean_up_dict)).strip().split(" ")
            for index in range(len(clean_line)-2):
                if tuple(clean_line[index:index+2]) not in trigram_dict:
                    trigram_dict.update({tuple(clean_line[index:index+2]): [clean_line[index+2]]})
                else:
                    trigram_dict[tuple(clean_line[index:index+2])].append(clean_line[index+2])
    return trigram_dict
