from account import Account

class ChildrensAccount(Account):
    def __init__(self, account_number, balance=0):
        super().__init__(account_number, balance)
        self.interest_rate = 0.007  # 0.7%

    def deposit(self, amount):
        super().deposit(amount)
        if amount > 0:
            interest = amount * self.interest_rate
            self._balance += interest
            print(f"Interest gained: {interest}. New balance: {self._balance}")

    def withdraw(self, amount):
        print("Withdrawals are not allowed for children's accounts.")
