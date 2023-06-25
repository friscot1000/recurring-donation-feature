import unittest
from DonationManager import DonationManager

expected_data = """['Donors:',
 'Jane: Total: $50 Average: $50.0',
 'John: Total: $100 Average: $100.0',
 '',
 'Campaigns:',
 'AnotherCampaign: Total: $50',
 'NewCampaign: Total: $100']"""


class TestDonationManager(unittest.TestCase):

    def setUp(self):
        self.donation_manager = DonationManager('input.txt')

    def test_add_campaign(self):
        self.donation_manager.add_campaign('add campaign TestCampaign')
        self.assertIn('TestCampaign', self.donation_manager.campaigns)

    def test_add_donor(self):
        self.donation_manager.add_donor('add donor Frank')
        self.assertIn('Frank', self.donation_manager.donors)

    def test_make_donation(self):
        self.donation_manager.add_campaign('add campaign TestCampaign')
        self.donation_manager.add_donor('add donor Frank')
        response = self.donation_manager.donate('donate Frank TestCampaign $100')
        self.assertEqual('Donation Successful', response)

    def test_donate_nonexistent_campaign(self):
        self.donation_manager.add_donor('add donor Mike')
        response = self.donation_manager.donate('donate Mike NonexistentCampaign $100')
        self.assertEqual('Campaign does not exist.', response)

    def test_donate_nonexistent_donor(self):
        self.donation_manager.add_campaign('add campaign TestCampaign')
        response = self.donation_manager.donate('donate Mike TestCampaign $100')
        self.assertEqual('Donor does not exist.', response)

    def test_output_file(self):
        self.donation_manager.add_donor('add donor John')
        self.donation_manager.add_donor('add donor Jane')

        self.donation_manager.add_campaign('add campaign NewCampaign')
        self.donation_manager.add_campaign('add campaign AnotherCampaign')

        self.donation_manager.donate('donate John NewCampaign $100')
        self.donation_manager.donate('donate Jane AnotherCampaign $50')

        self.donation_manager.write_donors()
        self.donation_manager.write_campaigns()

        with open('output/output.txt', 'r') as file1:
            file1_lines = file1.readlines()
            actual_data = [line.rstrip('\n') for line in file1_lines]

        self.assertEqual(eval(expected_data), actual_data)
        file1.close()


if __name__ == '__main__':
    unittest.main()
