#!/usr/bin/env python3


def create_table(column, data: dict):
    # Find the longest name to make large enough cell
    temp_list = list()
    for donor in data:
        temp_list.append(len(donor))

    for _ in column:
        temp_list.append(len(_))
    longest_space = sorted(temp_list)[-1] + 3
    print("\n\n\n")
    # Creating the table
    for item in column:
        print(item + (longest_space - len(item))*' ', end = '| ')
    print("\n")
    print("-"*longest_space*len(column))
    for donor in data:
        print(donor + (longest_space - len(donor))*' ', end = '| ')
        for item in data[donor]:
            print(str(item) + (longest_space - len(str(item)))*' ', end = '| ')
        print("\n")
