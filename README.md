# recurring-donation-feature

This repository contains a solution for a recurring donation feature. The solution allows for the management of donors, campaigns, and donations.

## Building and Running the Solution

### Clone the Repository

```shell
git clone https://github.com/friscot1000/recurring-donation-feature.git
```

### Run the Solution

From the root directory, run the following command:

```shell
./gfm-recurring input.txt
```

The results will be stored in the output folder in the `output.txt` file.

## Testing the Solution

To test the Donation Manager solution, follow the steps below:

1. Open a command prompt or terminal and navigate to the directory where the `DonationManagerTest.py` file is located.

2. Run the test script by executing the following command:

   ```bash
   python3 DonationManagerTest.py
   ```

## Solution Overview

The solution consists of three main files: `DonationManager`, `Donor`, and `Campaign`.

In the constructor, three objects are instantiated: `campaigns`, `donors`, and `filename`. The `main` method is used to call the constructor in `DonationManager`, and then the `user_input` method is called from that object.

Within the `user_input` method, the solution iterates over the text file and checks for specific keywords in each string. If any of the keywords are detected, a donor, a campaign, or donation is added accordingly.

Once all the necessary data is processed, the `write_donor()` and `write_campaigns()` methods are called to create the `output.txt` file.
