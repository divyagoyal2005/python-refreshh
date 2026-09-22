class BankAccount:
    bank_name = "ABC Bank"

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    @staticmethod
    def account_info():
        return "Bank accounts allow customers to deposit and withdraw money."

    def __str__(self):
        return f"{self.owner}'s account: ₹{self.balance}"

    def __repr__(self):
        return f"BankAccount(owner='{self.owner}', balance={self.balance})"

    def __eq__(self, other):
        return self.balance == other.balance


class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.05):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        self.balance += self.balance * self.interest_rate

    def __repr__(self):
        return (
            f"SavingsAccount(owner='{self.owner}', "
            f"balance={self.balance}, "
            f"interest_rate={self.interest_rate})"
        )


class CheckingAccount(BankAccount):
    def __init__(self, owner, balance=0, overdraft_limit=1000):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
        else:
            print("Withdrawal exceeds overdraft limit")


# Object creation
account1 = SavingsAccount("Divya", 5000)
account2 = CheckingAccount("Rahul", 3000)

account1.deposit(1000)
account1.add_interest()

account2.withdraw(3500)

print(account1)
print(repr(account1))
print(account2)

print(account1 == account2)

print(BankAccount.account_info())

BankAccount.change_bank_name("XYZ Bank")
print(BankAccount.bank_name)