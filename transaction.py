class Transaction:
    def __init__(self, date, description, amount, card):
        self.date = date
        self.description = description
        self.amount = amount
        self.card = card

    def __repr__(self):
        return f"Transaction({self.card}, {self.date}, {self.amount}, {self.description})"