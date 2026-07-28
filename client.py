# client.py

from account import Account


class Client:
    def __init__(self, f_name, l_name, user_id: int):
        self.f_name = f_name
        self.l_name = l_name
        self.user_id = user_id  # Unique user ID for each client
        self.accounts: dict[int, Account] = {}

    def get_info(self):
        return f"Client Name: {self.f_name} {self.l_name}, User ID: {self.user_id}"

    def create_account(self, account_number):
        if account_number in self.accounts:
            return f"Account number {account_number} already exists"
        new_account = Account(account_number)
        self.accounts[account_number] = new_account
        return f"Account {account_number} created"

    def print_accounts(self):
        if self.accounts:
            account_info = [account.print_balance()
                            for account in self.accounts.values()]
            return "\n".join(account_info)
        else:
            return "    ~0 ACTIVE ACCOUNTS~    "
