class BankAccount:
    def __init__(self, account_number, balance=0):
        """
        Constructor method to initialize the account number and balance.
        """
        self.account_number = account_number
        self.balance = balance
        self.no_funds = False

    def deposit(self, amount):
        """
        Method to deposit money into the account.
        """
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        """
        Method to withdraw money from the account.
        """
        if self.balance >= amount:
            self.balance -= amount
        elif amount > self.balance:
            self.no_funds = True

    def get_balance(self):
        """
        Method to retrieve the current balance.
        """
        if self.no_funds:
            return "Insufficient funds"
        else:
            return f"Account number: {self.account_number}\nCurrent balance: {self.balance:.2f}$"


class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance=0, interest_rate=0):
        """
        Constructor method to initialize the account number, balance, and interest rate.
        """
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        """
        Method to calculate and add interest to the account balance.
        """

        interest = self.interest_rate / 100
        interest_rate = self.balance * interest
        self.balance += interest_rate


# Testing the functionality of the classes with example information
# if __name__ == "__main__":
#     bank_account = BankAccount(123456789, 1000)
#     bank_account.deposit(500)
#     bank_account.withdraw(200)
#     print("\nBank Account: \n" + bank_account.get_balance())
#     savings_account = SavingsAccount(987654321, 2000, 5)
#     savings_account.deposit(1000)
#     savings_account.calculate_interest()
#     print(f"\nSavings Account without interest rate: \n{savings_account.get_balance()}")
#     print("Savings Account including interest rate: \n" + savings_account.get_balance())
#     print(f"Interest rate is: {savings_account.interest_rate}%")
