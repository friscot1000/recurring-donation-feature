import sys

campaigns = {}
donors = {}
donors_transactions = {}


def user_input():
    global line
    for line in sys.stdin:
        if 'add campaign' in line.rstrip().lower():
            print(line)
            add_campaign(line)
        elif 'add donor' in line.rstrip().lower():
            print(line)
            add_donor(line)
        elif 'donate' in line.rstrip().lower():
            donate(line)
        elif 'exit' == line.rstrip().lower():
            write_donors()
            write_campaigns()
            break
        else:
            print(f'Input : {line}')


def add_campaign(campaign):
    campaign_data = campaign.split()
    if campaign_data[2] not in campaigns:
        campaigns[campaign_data[2]] = 0
        print("Campaign " + campaign_data[2] + " added")


def add_donor(donor):
    donor_data = donor.split()[2]
    if donor_data not in donors:
        donors[donor_data] = 0
        donors_transactions[donor_data] = 0
        print("Donor " + donor_data + " added")


def donate(donation):
    donation_data = donation.split()
    # get amount
    amount = donation_data[3]
    # get donor
    donor = donation_data[1]
    # see if campaign exist
    # add amount to existing campaign
    campaign = donation_data[2]
    if campaign in campaigns:
        campaigns[campaign] += int(amount)
    else:
        print("does not exist")
    # See if user exist and add amount to existing user
    if donor in donors and donor in donors_transactions:
        donors[donor] += int(amount)
        donors_transactions[donor] += 1


def write_donors():
    with open('output/output.txt', 'w') as output:
        output.write('Donors:'.title() + '\n')
        for donor in donors:
            average_donation = get_average_donation(donor)
            output.write(
                donor.capitalize() + ': Total: $' + str(donors[donor]) + ' Average: $' + str(average_donation) + '\n')


def get_average_donation(donor):
    return donors[donor] / donors_transactions[donor]


def write_campaigns():
    with open('output/output.txt', 'a') as output:
        output.write('\n' + 'Campaigns:'.title() + '\n')
        for campaign in campaigns:
            output.write(campaign + ': Total: $' + str(campaigns[campaign]) + '\n')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    user_input()
