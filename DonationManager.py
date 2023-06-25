import sys

from Campaign import Campaign
from Donor import Donor


class DonationManager:
    def __init__(self):
        self.campaigns = {}
        self.donors = {}

    def user_input(self):
        for user_input in sys.stdin:
            user_input = user_input.strip().lower()
            if 'add campaign' in user_input:
                self.add_campaign(user_input)
            elif 'add donor' in user_input:
                self.add_donor(user_input)
            elif 'donate' in user_input:
                self.donate(user_input)
            elif 'exit' == user_input:
                self.write_donors()
                self.write_campaigns()
                break
            else:
                print(f'Input: {user_input}')

    def add_campaign(self, user_input):
        campaign_data = user_input.split()
        campaign_name = campaign_data[2]
        if campaign_name not in self.campaigns:
            self.campaigns[campaign_name] = Campaign(campaign_name)
            print(f"Campaign {campaign_name} added")

    def add_donor(self, user_input):
        donor_data = user_input.split()
        donor = donor_data[2]
        print(donor)
        if donor not in self.donors:
            self.donors[donor] = Donor(donor)
            print(f"Donor {donor} added")

    def donate(self, user_input):
        donation_data = user_input.split()
        donor_name = donation_data[1]
        campaign_name = donation_data[2]
        amount = int(donation_data[3])

        if campaign_name in self.campaigns:
            self.campaigns[campaign_name].make_donation(amount)
        else:
            print("Campaign does not exist.")
        if donor_name in self.donors:
            self.donors[donor_name].donation(amount)
        else:
            print("Donor does not exist.")
        print("Thank you " + donor_name + " for your donation of " + str(amount) + ' benefiting ' + campaign_name)

    def write_donors(self):
        with open('output/output.txt', 'w') as output:
            output.write('Donors:\n')
            for donor in self.donors.values():
                output.write(str(donor) + '\n')

    def write_campaigns(self):
        with open('output/output.txt', 'a') as output:
            output.write('\nCampaigns:\n')
            for campaign in self.campaigns.values():
                output.write(str(campaign) + '\n')


if __name__ == '__main__':
    donation_manager = DonationManager()
    donation_manager.user_input()
