class Campaign:
    def __init__(self, name):
        self.name = name
        self.total_amount = 0

    def make_donation(self, amount):
        self.total_amount += amount

    def __str__(self):
        return f"{self.name}: Total: ${self.total_amount}"
