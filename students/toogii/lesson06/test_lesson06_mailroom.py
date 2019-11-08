from lesson06_mailroom import create_report,main,create_table,send_a_thank_you,get_a_new_donor_info,list_all_donors,update_donation,send_letters_to_all_donors,email_compose

choices = ('Choice_1', 'Choice_2','Choice_3','Choice_4')
donations = {'donor_1': {"donation": 3, "donation_amnt": 30000},'donor_2': {"donation": 4, "donation_amnt": 5000}}

def test_create_report():
    assert create_report(donations)is {'donor_1': [3, 30000, 10000.0],'donor_2': [4, 5000, 1666.6666666666667}}
