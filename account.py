# account.py

class Account:
    def __init__(self, account_number):
        self.account_number = account_number # Unique account number for each account
        self.__balance = 0
        self.account = account_number

    def deposit(self, amount):
        self.__balance += amount
        return f"Deposited {amount}. New balance: ${self.__balance}"

    def withdraw(self, amount):
        if amount > self.__balance:
            return "Insufficient funds"
        self.__balance -= amount
        return f"Withdrew {amount}. New balance: ${self.__balance}"

    def print_balance(self):
        return f"Account {self.account_number} balance: ${self.__balance}"
