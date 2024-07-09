"""
Design a class representing a bank account. Include attributes like balance, account holder, 
and methods for deposit, withdrawal, and displaying balance.
"""
import sys

class BankAccount:
    def __init__(self, balance:int, account_holder:str):
        # what does self mean? 
        self.balance = balance
        self.account_holder = account_holder

    def getBalance(self):
        return self.balance
    
    def deposit(self, amount):
        self.balance += amount
        return f"{amount:.2f} added to your account."

    # make sure the amount withdrawn is less than total balance
    def withdrawal(self, amount):
        if amount > self.balance:
            return "Insufficient funds. Withdraw failed."

        self.balance -= amount
        return f"${amount:.2f} added to your account."
        

    def display_balance(self):
        return f"\nHello {self.account_holder}, You have a total of ${self.balance:.2f} in your account."


## MAIN ##
# create an instance of our BankAccount class
lauren = BankAccount(100, "Lauren")
lauren.display_balance()

# extra: a text based interface for the class
print("Welcome to Bank of Python:")
is_active = True
while is_active:
    user_action = input("\n[W] to Withdraw money.\n[D] to Deposit.\n[C] to check and display your current balance.\n[Q] to quit.\nType here: ").upper()
    match user_action:
        case "W":
            withdraw_amount = int(input("\nHow much money would you like to withdraw? "))
            print(lauren.withdrawal(withdraw_amount))
        case "D":
            deposit_amount = int(input("\nHow much money would you like to deposit? "))
            print(lauren.deposit(deposit_amount))
        case "C":
            print(lauren.display_balance())
        case "Q":
            print("Goodbye.")
            is_active = False
            sys.exit()
        case _:
            print("Invalid choice.")
