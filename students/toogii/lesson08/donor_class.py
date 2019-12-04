#!/usr/bin/env python3


from datetime import date, datetime

class Donor:
    donation_dict = {}
    email_template = "Date {}, Dear {}, Thank you for your contribution of {} to our charity. "
    def __init__(self,name,donation_amount,donations=1):
        self.name = name
        self.last_donation_amount = donation_amount
        self.donations = donations
        self.average_donation = donation_amount/donations
        Donor.donation_dict.update({self.name:{'donations': self.donations, 'donation_amount': self.last_donation_amount, 'average_donation': self.average_donation }})


    def __repr__(self):
        return self.name

    def add_donation(self,last_donation_amount):
        self.last_donation_amount = last_donation_amount
        Donor.donation_dict[self.name]['donation_amount'] = Donor.donation_dict[self.name]['donation_amount'] + self.last_donation_amount
        Donor.donation_dict[self.name]['donations'] = Donor.donation_dict[self.name]['donations'] + 1 
        Donor.donation_dict[self.name]['average_donation'] = Donor.donation_dict[self.name]['donation_amount']/Donor.donation_dict[self.name]['donations']
        self.average_donation = Donor.donation_dict[self.name]['donation_amount']/Donor.donation_dict[self.name]['donations']

        
    def email(self):
        print(Donor.email_template.format(str(datetime.today()).split(".")[0],self.name, self.last_donation_amount))

    def email_to_all_donors(self):
        for donor in Donor.donation_dict:
            print("\n\n")
            print(Donor.email_template.format(str(datetime.today()).split(".")[0],donor, Donor.donation_dict[donor]['donation_amount']))

    def total_donation(self):
    	return sum(Donor.donation_dict[self.name])

    def charity_total_donation(self):
    	self.lst = []
    	for _ in list(Donor.donation_dict.values()):
    		self.lst.append(sum(_))
    	return(sum(self.lst))

    def remove_donor(self):
        Donor.donation_dict.pop(self.name)
        return '{} have been removed'.format(self.name)

    def list_all_donors(self):
        if Donor.donation_dict:
            for number, donor in enumerate(Donor.donation_dict):
                print('{}. {}' .format(number + 1, donor))
        else:
            print("Donor list is empty!")

             
   
