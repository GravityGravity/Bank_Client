# Main.py

#DESC: This is a simple banking application that allows users to create clients and manage their accounts. The application provides basic functionalities such as depositing and withdrawing money from an account.

from client import Client

client1 = Client("John", "Doe", 1)
print(client1.get_info())

print(client1.create_account(12345))
print(client1.create_account(10013))
print(client1.create_account(12345))

print(client1.print_accounts())

print(client1.accounts[0].deposit(500))
print(client1.accounts[0].print_balance())
print(client1.accounts[0].print_balance())
