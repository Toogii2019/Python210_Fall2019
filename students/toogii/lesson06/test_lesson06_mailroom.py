#!/usr/bin/env python3
import lesson06_mailroom
import unittest
from unittest.mock import patch
import containers
from datetime import date


donations_dict_dict = {'donor_name_1': {"donation": 3, "donation_amnt": 30000},'donor_name_2': {"donation": 2, "donation_amnt": 5000}, 'donor_name_3': {"donation": 5, "donation_amnt": 155000}, 'donor_name_4': {"donation": 2, "donation_amnt": 500}, 'donor_name_5': {"donation": 2, "donation_amnt": 10000}}
lst_names = [(1, 'donor_name_1'), (2,'donor_name_2'), (3, 'donor_name_3'),(4, 'donor_name_4'),(5, 'donor_name_5')]
donations_dict_list = {'donor_name_1': [3, 30000, '10000.0'],'donor_name_2': [ 2, 5000, '2500.0'], 'donor_name_3': [ 5,  155000, '31000.0'], 'donor_name_4': [ 2, 500, '250.0'], 'donor_name_5': [ 2,  10000, '5000.0']}
column = ['Donor Name', 'Num Gifts', 'Total Given ($)', 'Average Gift ($)']

email_letter = "\n\nDear {},\n\nThank you for your generous gift of $ {} to our organization. We are thrilled to have your support.\nThrough your donation we have been able to accomplish our charity work around the world.\n  \nThank you\n\n"

class TestCalc(unittest.TestCase):



    def test_create_report(self):
        result = lesson06_mailroom.create_report(donations_dict_dict)
        self.assertEqual(result, donations_dict_list)


    def test_create_table(self):
        lst = list()
        for donor in donations_dict_dict:
            lst.append(len(donor))
        self.assertEqual(lesson06_mailroom.create_table(column, donations_dict_list), sorted(lst)[-1] + 3)


    def test_list_all_donors(self):
        self.assertEqual(lesson06_mailroom.list_all_donors(donations=donations_dict_dict), lst_names)


    def test_update_donation(self):
#        self.assertEqual(lesson06_mailroom.update_donation('donor_name_2', 5501, donations_dict_dict), (3, 10501))
        self.assertEqual(lesson06_mailroom.update_donation('donor_name_2', 5501, donations_dict_dict), (donations_dict_dict['donor_name_2']['donation'], donations_dict_dict['donor_name_2']['donation_amnt']))


    def test_email_compose(self):
        self.assertEqual(lesson06_mailroom.email_compose('donor_name_1', 30000), (email_letter.format('donor_name_1', 30000)))    


    def test_send_letters_to_donors(self):
        self.donor = 'donor name_1'
        self.donations_dict = {'donor name_1': {"donation": 3, "donation_amnt": 30000}}
        self.filename = "_".join(self.donor.split()) + '_' + "_".join(str(date.today()).split("-")) + '_' + "donation" + "_" + str(self.donations_dict[self.donor]["donation"])
        self.assertEqual(lesson06_mailroom.send_letters_to_all_donors(donations=self.donations_dict), (self.filename, self.donor)) 

if __name__ == '__main__':
    unittest.main()
