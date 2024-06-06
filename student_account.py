from account import Account

class StudentAccount(Account):
    def __init__(self, account_number, balance=0):
        super().__init__(account_number, balance)

    def deposit(self, amount):
        if amount <= 50000:
            super().deposit(amount)
        else:
            print("Deposit amount exceeds the limit of 50,000 per deposit.")

    def withdraw(self, amount):
        if amount <= 2000:
            super().withdraw(amount)
        else:
            print("Withdrawal amount exceeds the limit of 2,000.")
