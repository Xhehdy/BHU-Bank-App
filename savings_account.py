from account import Account

class SavingsAccount(Account):
    def __init__(self, account_number, balance=0):
        super().__init__(account_number, balance)
        self.interest_rate = 0.005  # 0.5%

    def deposit(self, amount):
        super().deposit(amount)
        if amount > 0:
            interest = amount * self.interest_rate
            self._balance += interest
            print(f"Interest gained: {interest}. New balance: {self._balance}")

    def withdraw(self, amount):
        if amount <= 700000:
            super().withdraw(amount)
        else:
            print("Withdrawal amount exceeds the limit of 700,000.")
