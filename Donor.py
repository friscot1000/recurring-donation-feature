class Donor:
    def __init__(self, name):
        self.name = name
        self.total_donations = 0
        self.number_of_transactions = 0

    def donation(self, amount):
        self.total_donations += amount
        self.number_of_transactions += 1

    def get_average_donation(self):
        if self.number_of_transactions == 0:
            return 0
        return self.total_donations / self.number_of_transactions

    def __str__(self):
        average_donation = self.get_average_donation()
        return f"{self.name.capitalize()}: Total: ${self.total_donations} Average: ${average_donation}"
