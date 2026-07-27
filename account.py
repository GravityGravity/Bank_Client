# account.py

from transaction import Transaction

class Account:
    def __init__(self, account_number):
        self.account_number = account_number # Unique account number for each account
        self.__balance = 0
        self.account = account_number
        self.transactions = [] # List to store transactions for the account

    def deposit(self, amount):
        if amount <= 0:
            return "Deposit amount must be positive"
        self.__balance += amount
        self.transactions.append(Transaction(len(self.transactions), amount, "deposit", self.__balance - amount))
        return f"Deposited {amount}. New balance: ${self.__balance}"

    def withdraw(self, amount):
        if amount <= 0:
            return "Withdrawal amount must be positive"
        if amount > self.__balance:
            return "Insufficient funds"
        self.__balance -= amount
        self.transactions.append(
            Transaction(len(self.transactions), amount, "withdrawal", self.__balance + amount))
        return f"Withdrew {amount}. New balance: ${self.__balance}"

    def print_balance(self):
        return f"Account {self.account_number} balance: ${self.__balance}"

    def print_transactions(self, account_number):
        if account_number != self.account_number:
            return "Invalid account number"
        if not self.transactions:
            return "No transactions found"
        
        transaction_history = [f"Transaction ID: {t.transaction_id}, Type: {t.transaction_type}, Amount: {t.amount}, Balance After Transaction: {t.balance_after_transaction}, Time: {t.time}" for t in self.transactions]
        return "\n".join(transaction_history)
