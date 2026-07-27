# Main.py

#DESC: This is a simple banking application that allows users to create clients and manage their accounts. The application provides basic functionalities such as depositing and withdrawing money from an account.

#Initial Code Plan Created by: Group 2: Jason L, Ibrahim T, Isaak H

class Client:
    def __init__(self, f_name, l_name, user_id):
        self.f_name = f_name
        self.l_name = l_name
        self.user_id = user_id #Unique user ID for each client
        self.accounts = [] # Review: Most likely will need to change this to a key-value pair to store account numbers and their corresponding balances

    def get_info(self):
        return f"Client Name: {self.f_name} {self.l_name}, User ID: {self.user_id}"

    def create_account(self, account_number):
        if account_number in [account.account_number for account in self.accounts]:
            return f"Account number {account_number} already exists"
        new_account = Account(account_number)
        self.accounts.append(new_account)
        return f"Account {account_number} created" 

    def print_accounts(self):
        account_info = [account.print_balance() for account in self.accounts]
        return "\n".join(account_info)

class Account:
    def __init__(self, account_number):
        self.account_number = account_number #Unique account number for each account
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


client1 = Client("John", "Doe", 1)
print(client1.get_info())

print(client1.create_account(12345))
print(client1.create_account(10013))
print(client1.create_account(12345))

print(client1.print_accounts())

print(client1.accounts[0].deposit(500))
print(client1.accounts[0].print_balance())
print(client1.accounts[0].print_balance())
