#!/usr/bin/env python3
from time import sleep
from datetime import date, datetime
import sys
import os


choices = ('Send a Thank You', 'Create Report','Send letters to all donors','Quit')
donations = {'TOOGII DASHDAVAA': {"donation": 3, "donation_amnt": 30000},'MARK ZACHERBERG': {"donation": 4, "donation_amnt": 5000}, 'JEFF BEZOS': {"donation": 5, "donation_amnt": 155000}, 'BILL GATES': {"donation": 1, "donation_amnt": 500}, 'LARRY PAGE': {"donation": 2, "donation_amnt": 10000}}


def email_compose(donor : str, donation_amount: int):
    # Generate and print an appreciation email to new Donor.
    email_letter = "Date: {}\n\nDear {},\n\nThank you for your generous gift of $ {} to our organization. We are thrilled to have your support.\nThrough your donation we have been able to accomplish our charity work around the world.\n  \nThank you\n\n" .format(str(datetime.today()).split(".")[0], donor,donation_amount)
    print("\n\nGenerating an appreciation email for {}!\n\n" .format(donor))
    sleep(1)
    print("="*30)
    print("\n{}".format(email_letter))
    print("="*30)
    sleep(1)
    return email_letter


def send_letters_to_all_donors():
    '''
    This function creates a folder called "files" in the working directly and writes email files.
    If new donation received from the donor, the new file will be created. If not, the function will not create nor write to a existing file.
    '''
    for donor in donations:
        filename = "_".join(donor.split()) + '_' + "_".join(str(date.today()).split("-")) + '_' + "donation" + "_" + str(donations[donor]["donation"])
        if not os.path.exists(os.path.abspath('files')):
            os.mkdir('files')
        if filename in os.listdir('files'):
            print("There are no new donations for {} and the email {} already exists!. Skipping!" .format(donor, filename))
            continue
        with open(os.path.abspath('files/' + filename), 'a') as email:
            email.write(email_compose(donor, donations[donor]["donation_amnt"]))
            print("="*30)
            print("The file {} for {} has been created!" .format(filename, donor))


def update_donation(donor, donation_amnt):
    # Update dictionary of donors with new donor information.
    if donor in donations:
        donations[donor]["donation"] = donations[donor]["donation"] + 1
        donations[donor]["donation_amnt"] = donations[donor]["donation_amnt"] + donation_amnt
    else:
        donations.update({donor: {"donation": 1,"donation_amnt": donation_amnt }})


def list_all_donors():
    # Prints all Donors
    for index, donors in enumerate(donations):
        print(str(index + 1) + " -- " + donors)


def get_a_new_donor_info():
    # Get the Donor name and donation amount
    while True:
        donor = str(input("\nEnter the full name of the Donor or type list to list all existing Donors(or enter QUIT to go back to main menu):   "))
        print("\nYour Entered {} \n\n" .format(donor.upper()))
        sleep(1)
        if donor.upper() == "LIST":
            list_all_donors()
            continue
        if donor.upper() == 'QUIT':
            main(called=True)
            continue
        while True:
            donation_amount = input('Please enter the donation amount of {} (or enter QUIT to go back to main menu) ? :  '.format(donor))
            if donation_amount.upper() == 'QUIT':
                main(called=True)
                continue
            return donor.upper(), int(donation_amount)


def send_a_thank_you():
    # Gather Information about the new Donor
    donor,donation_amount = get_a_new_donor_info()
    sleep(1)
    update_donation(donor.upper(),int(donation_amount))
    email_compose(donor, donation_amount)


def create_table(column, data: dict):
    # Find the longest name to make large enough cell
    temp_list = list()
    for donor in data:
        temp_list.append(len(donor))
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


def create_report():
    # Prepare the Data for creating the table
    column = ['Donor Name', 'Num Gifts', 'Total Given ($)', 'Average Gift ($)']
    data = dict()
    # Creating dict-of-list for the table.
    for donor in donations:
        data.update({donor: []})
        for k, v in donations[donor].items():
            data[donor].append(v)
        data[donor].append(str(data[donor][-1]/data[donor][-2]))
    create_table(column,data)


choice_dict = {'1': send_a_thank_you, '2': create_report, '3': send_letters_to_all_donors, '4': 'QUIT'}


def main(called=False):
    #Getting a user input
    while True:
        print('\n\n\n\t Welcome to Donations!\n\n')
        print('\t1.   {}\n\t2.   {}\n\t3.   {}\n\t4.   {}'.format(*choices))
        if called == True:
            print('\n\n\n\tHit R to go resume where you left')
        choice = input("\n\nPlease Enter Your choice:   ".format(choices))
        sleep(1)
        if str(choice).upper() == 'R':
            return None
        if choice_dict.get(str(choice),None):
            if choice_dict[str(choice)] == 'QUIT':
                sleep(1)
                print('\n\nExiting the program!\n\nHave a good day!\n\n')
                sleep(1)
                sys.exit('Good Bye')
            choice_dict[str(choice)]()
        else:
            choice_dict.popitem()
            print("Please enter the valid choice!")


if __name__ == '__main__':
    main()
