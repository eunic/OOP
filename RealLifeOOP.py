class BankAccount(object):

    def __init__(self):

        pass

    def withdraw(self):

        pass

    def deposit(self):

        pass

    def getBalance(self):

        pass 



class SavingsAccount(BankAccount):

    def __init__(self):
        self.balance = 500

    def deposit(self):

        cash_deposited = input("Please enter Amount to Deposit")

        if cash_deposited < 0:

            print("Invalid deposit amount")

        else:
            self.balance += cash_deposited

            print("You have deposited %d and your balance is now %d"%(cash_deposited, self.balance))


    def withdraw(self):

        amount = input("Please enter Amount to withdraw")

        if amount < 0:

            print("Invalid withdraw amount")

        elif amount > self.balance:

            print("Cannot withdraw beyond the current account balance")

        else:
            self.balance -= amount

            if self.balance < 500:

                print("Cannot withdraw beyond the minimum account balance 500")

            else:

                print("You have deposited %d and your balance is now %d"%(cash_deposited, self.balance))

    def getBalance(self):

        print("your balance is now %d"%(self.balance))



class CurrentAccount(BankAccount):

    def __init__(self):

        self.balance = 0

    def deposit(self):

        amount = input("Please enter Amount to Deposit")

        if amount < 0:

            print("Invalid deposit amount")

        else:
            self.balance += amount

            print("You have deposited %d and your balance is now %d"%(amount, self.balance))

    def withdraw(self):

        withdrawamount = input("Please enter Amount to withdraw")

        if withdrawamount < 0:

            print("Invalid withdraw amount")

        elif withdrawamount > self.balance:

            print("Cannot withdraw beyond the current account balance")

        else:

            self.balance -= withdrawamount

            print("You have deposited %d and your balance is now %d"%(amount, self.balance))

    def getBalance(self):

        print("your balance is now %d"%(self.balance))


account = input("please choose 1 for SavingsAccount and 2 for CurrentAccount")

if account == 1:

    s = SavingsAccount()

    choose = input("please choose 1 for deposit and 2 for withdraw and 3 for balance Inquiry")

    if choose == 1:

        s.deposit()
    elif choose == 2:

        s.withdraw()

    elif choose == 3:
        s.getBalance()

    else:
        print("Incorrect Entry")


elif account == 2:

    c= CurrentAccount()

    choose = input("please choose 1 for deposit and 2 for withdraw and 3 for balance Inquiry")

    if choose == 1:

        c.deposit()
    elif choose == 2:

        c.withdraw()

    elif choose == 3:
        c.getBalance()

    else:
        print("Incorrect Entry")
    

else:
    print("Incorrect Entry")