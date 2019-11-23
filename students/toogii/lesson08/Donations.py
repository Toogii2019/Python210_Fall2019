#!/usr/bin/env python3


from datetime import date, datetime

class Donor:
    donation_dict = {}
    email_template = "Date {}, Dear {}, Thank you for your contribution of {} to our charity. "
    def __init__(self,name,donation_amount,donations=1):
        self.name = name
        self.last_donation_amount = donation_amount
        self.donations = donations
        Donor.donation_dict.update({self.name:{'donation_amount': self.last_donation_amount, 'donations': self.donations}})

    def add_donation(self,last_donation_amount):
    	self.last_donation_amount = last_donation_amount
        Donor.donation_dict[self.name]['donation_amount'] = Donor.donation_dict[self.name]['donation_amount'] + self.last_donation_amount
        
    def email(self):
        print(Donor.email_template.format(str(datetime.today()).split(".")[0],self.name, self.donation_amount))
    def email_to_all_donors(self):
        for donor in Donor.donation_dict:
            print("\n\n")
            print(Donor.email_template.format(str(datetime.today()).split(".")[0],donor, Donor.donation_dict[donor]))
    def total_donation(self):
    	return sum(Donor.donation_dict[self.name])
    def average_donation(self):
        return sum(Donor.donation_dict[self.name])/len(Donor.donation_dict[self.name])
    def charity_total_donation(self):
    	self.lst = []
    	for _ in list(Donor.donation_dict.values()):
    		self.lst.append(sum(_))
    	return(sum(self.lst))

             
   
