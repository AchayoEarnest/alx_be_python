#!/usr/bin/env python3

class BankAccount:
    def __init__(self, initial_balance: 0):
        """Initializing account with default optonal balance"""
        self.__account_balance = initial_balance
        

    def deposit(self, amount):
        """adds the specified ammount to the current balance"""
        if amount > 0:
            self.__account_balance += amount
    
    def withdraw(self, amount):
        """Deduct ammount if current amount is not insufficient"""
        if amount > 0 and amount <= self.__account_balance:
            return True
        return False
    
    def display_balance(self):
        """Print the current account balance"""
        print(f"Current Balance: ${self.__account_balance:.2f}")