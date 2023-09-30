# https://www.codewars.com/kata/5a03af9606d5b65ff7000009


class User:
    def __init__(self, name, balance=0, checking_account=None):
        self.name = name
        self.balance = balance
        self.checking_account = checking_account
    
    def add_cash(self, amount_to_add):
        self.balance += amount_to_add
        return f"{self.name} has {self.balance}."
    
    def withdraw(self, amount_to_withdraw):
        try:
            if self.balance >= amount_to_withdraw:
                self.balance -= amount_to_withdraw
                return f"{self.name} has {self.balance}."
            raise ValueError(f"{self.name} can't withdraw {amount_to_withdraw}, he only has {self.balance}.")
        except ValueError as e:
            return e

    def check(self, other_user, amount_to_transfer):
        try:
            if other_user.balance >= amount_to_transfer:
                if other_user.checking_account:
                    other_user.balance -= amount_to_transfer
                    self.balance += amount_to_transfer
                    return f"{self.name} has {self.balance} and {other_user.name} has {other_user.balance}."
                raise ValueError(f"{other_user.name}'s checking account is disabled.")
            raise ValueError(f"{other_user.name} doesn't have enough money.")
        except ValueError as e:
            return e




Jeff = User('Jeff', 70, True)
Joe = User('Joe', 70, False)

print(Jeff.withdraw(2))
print(Joe.check(Jeff, 50))
print(Jeff.check(Joe, 80))
print(Jeff.add_cash(20))
print(Jeff.withdraw(120))
print(Joe.check(Jeff, 800))