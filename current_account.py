from account import Account

class CurrentAccount(Account):
    def __init__(self, account_number, balance=0):
        super().__init__(account_number, balance)
        # No additional restrictions for current accounts
