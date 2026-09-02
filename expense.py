class Expense:
    def __init__(self, amount, category, date, note):
        self.amount = amount
        self.category = category
        self.date = date
        self.note = note

    def __str__(self):
        return(
            f"Date: {self.date}  |"
            f"Category: {self.category}  |"
            f"Amount: {self.amount}  |"
            f"Note: {self.note}  |"
        )


