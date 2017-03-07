class BankAccount(object):
    def __init__(self):

        pass

    def withdraw(self):

        pass

    def deposit(self):

        pass


class SavingsAccount(BankAccount):

    def __init__(self):
        self.balance = 500

    def deposit(self,cash_deposited):

        if cash_deposited < 0:

            return "Invalid deposit amount"

        else:
            self.balance += cash_deposited
            return self.balance

    def withdraw(self, amount):
        if amount < 0:
            return "Invalid withdraw amount"
        elif amount > self.balance:
            return "Cannot withdraw beyond the current account balance"
        else:
            self.balance -= amount
            if self.balance < 500:
                return "Cannot withdraw beyond the minimum account balance"
            else:
                return self.balance


class CurrentAccount(BankAccount):

    def __init__(self):
        self.balance = 0

    def deposit(self,amount):
        if amount < 0:

            return "Invalid deposit amount"

        else:
            self.balance += amount

            return self.balance

    def withdraw(self,withdrawamount):

        if withdrawamount < 0:
            return "Invalid withdraw amount"
        elif withdrawamount > self.balance:
            return "Cannot withdraw beyond the current account balance"
        else:
            self.balance -= withdrawamount
            return self.balance