from savings_account import SavingsAccount
from current_account import CurrentAccount
from childrens_account import ChildrensAccount
from student_account import StudentAccount

# Example usage:
savings_account = SavingsAccount("SA123")
savings_account.deposit(10000)
savings_account.withdraw(500)

current_account = CurrentAccount("CA123")
current_account.deposit(20000)
current_account.withdraw(10000)

childrens_account = ChildrensAccount("CH123")
childrens_account.deposit(5000)
childrens_account.withdraw(1000)

student_account = StudentAccount("ST123")
student_account.deposit(40000)
student_account.withdraw(1500)
student_account.deposit(60000)
student_account.withdraw(3000)
