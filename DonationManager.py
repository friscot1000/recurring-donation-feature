import sys
from collections import OrderedDict
from Campaign import Campaign
from Donor import Donor


class DonationManager:
    def __init__(self, filename):
        self.campaigns = {}
        self.donors = {}
        self.filename = filename

    def user_input(self):
        with open(self.filename, "r") as data:
            for line in data:
                text_input = line.lower().strip()
                if 'add campaign' in text_input:
                    self.add_campaign(text_input)
                elif 'add donor' in text_input:
                    self.add_donor(text_input)
                elif 'donate' in text_input:
                    self.donate(text_input)
            self.write_donors()
            self.write_campaigns()
            print("")

    def add_campaign(self, user_input):
        campaign_data = user_input.split()
        campaign_name = campaign_data[2]
        if campaign_name not in self.campaigns:
            self.campaigns[campaign_name] = Campaign(campaign_name)

    def add_donor(self, user_input):
        donor_data = user_input.split()
        donor = donor_data[2]
        if donor not in self.donors:
            self.donors[donor] = Donor(donor)

    def donate(self, user_input):
        donation_data = user_input.split()
        donor_name = donation_data[1]
        campaign_name = donation_data[2]
        amount = int(donation_data[3].strip('$'))

        if campaign_name in self.campaigns:
            self.campaigns[campaign_name].make_donation(amount)
        else:
            print("Campaign does not exist.")
        if donor_name in self.donors:
            self.donors[donor_name].donation(amount)
        else:
            print("Donor does not exist.")

    def write_donors(self):
        sorted_donors = OrderedDict(sorted(self.donors.items()))
        with open('output/output.txt', 'w') as output:
            output.write('Donors:\n')
            for donor in sorted_donors.values():
                output.write(str(donor) + '\n')

    def write_campaigns(self):
        sorted_campaigns = OrderedDict(sorted(self.campaigns.items()))
        with open('output/output.txt', 'a') as output:
            output.write('\nCampaigns:\n')
            for campaign in sorted_campaigns.values():
                output.write(str(campaign) + '\n')


if __name__ == '__main__':
    donation_manager = DonationManager(sys.argv[1])
    donation_manager.user_input()
