from datetime import datetime

class Transaction:
    def __init__(self, transaction_id: int, amount: float, transaction_type: str, balance_before_transaction: float):
        self.transaction_id = transaction_id
        self.amount = amount
        self.transaction_type = transaction_type # 'deposit' or 'withdrawal'
        self.balance_after_transaction = balance_before_transaction + (-amount if transaction_type == 'withdrawal' else amount)  # This will be set after the transaction is processed
        self.time = datetime.now()  # Timestamp of the transaction