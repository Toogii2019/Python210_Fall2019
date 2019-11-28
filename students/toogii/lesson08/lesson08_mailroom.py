#!/usr/bin/env python3
from donor_class import Donor
from time import sleep
from table_creator import create_table
import sys


donor_obj_dict = dict()
choices = ('Send a Thank You', 'Create Report','Send letters to all donors','Quit')


def get_donor_info():
    while True:
        donor = input("Please enter the donor name or list to list all the existing Donors:    ")
        if donor.upper() == 'LIST':
            Donor.list_all_donors('self')
            continue
        while True:
            try:
                donation_amnt = int(input("Please enter the donation amount:   "))
            except ValueError:
                print("Please enter the valid amount:  ")
                continue
            else:
                print("\n\nYou entered {} with {} amount of donation.\n\n" .format(donor,donation_amnt))
                break
        break
    return donor,donation_amnt


def create_report():
    column = ['Donor Name', 'Num Gifts', 'Total Given ($)', 'Average Gift ($)']
    data = {donor: [v for k, v in Donor.donation_dict[donor].items()] for donor in Donor.donation_dict}
    create_table(column,data)
    return data


def send_letters_to_all_donors():
    try:
        Donor.email_to_all_donors(list(Donor.donation_dict.keys())[0])
    except IndexError:
        print("The donor list is empty!")
    else:
        print("==============================")
        print("\n\nEmail successfully sent to all Donors")
    return None


def send_a_thank_you():
    donor_name, donation_amnt = get_donor_info()
    if not donor_name.upper() in Donor.donation_dict:
        new_donor = Donor(donor_name.upper(),donation_amnt)
        new_donor.email()
        donor_obj_dict.update({donor_name: new_donor})
    else:
        donor_obj_dict[donor_name].add_donation(donation_amnt)
        donor_obj_dict[donor_name].email()
    return None


choice_dict = {'1': send_a_thank_you, '2': create_report, '3': send_letters_to_all_donors, '4': 'QUIT'}


def main(called=False):

    while True:
        print('\n\n\n\t Welcome to Donations!\n\n')
        print('\t1.   {}\n\t2.   {}\n\t3.   {}\n\t4.   {}'.format(*choices))
        if called == True:
            print('\n\n\n\tHit R to go resume where you left')
        choice = input("\n\nPlease Enter Your choice:   ".format(choices))
        sleep(1)
        if str(choice).upper() == 'R':
            break
        if choice_dict.get(str(choice),None):
            if choice_dict[str(choice)] == 'QUIT':
                sleep(1)
                print('\n\nExiting the program!\n\nHave a good day!\n\n')
                sleep(1)
                sys.exit("Program quit by user request")
            choice_dict[str(choice)]()
        else:
            choice_dict.popitem()
            print("Please enter the valid choice!")


if __name__ == '__main__':
    main()
