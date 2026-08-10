from account import Account
from exceptions import AccountNotFound, LowBalance

class Bank:
    def __init__(self):
        self.accounts = {}
        self.next_account_no = 1001

    def create_account(self, name, balance):
        account = Account(self.next_account_no, name, balance)
        self.accounts[self.next_account_no] = account
        self.next_account_no += 1
        return account

    def find_account(self, account_no):
        if account_no not in self.accounts:
            raise AccountNotFound("Account not found")
        return self.accounts[account_no]

    def deposit(self, account_no, amount):
        account = self.find_account(account_no)
        account.deposit(amount)

    def withdraw(self, account_no, amount):
        account = self.find_account(account_no)
        if amount > account.balance:
            raise LowBalance("Insufficient balance")
        account.withdraw(amount)

    def balance(self, account_no):
        account = self.find_account(account_no)
        return account.show_balance()