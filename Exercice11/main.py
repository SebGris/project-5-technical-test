class BankAccount:
    def __init__(self, account_holder: str, balance: float = 0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def display_balance(self):
        print(f"Titulaire du compte : {self.account_holder}")
        print(f"Solde du compte : {self.balance}")
