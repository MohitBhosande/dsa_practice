# python banking program


import numpy 

import os

class Balance:
    def __init__(self):
        self.amount = 0.0

    def show_balance(self):
        print(f"your balance is ${self.amount:.2f}")

    def deposit(self):
        amount = float(input("enter the amount you want to deposit: "))

        if amount <= 0:
            print("the amount is invalid")
            return self.amount

        self.amount += amount
        print(f"deposit successful: ${amount:.2f}")
        return self.amount

    def withdraw(self, accntno, password):
        amount = float(input("enter the amount you want to withdraw: "))
        
        if amount <= 0:
            print("the amount is invalid")
            return self.amount

        if amount > self.amount:
            print("insufficient balance!!")
            if self.amount <= 0:
                print("your balance is too low!!")
            return self.amount

        self.amount -= amount
        print(f"withdrawal successful: ${amount:.2f}")
        return self.amount


account = Balance()
is_running = True
a = input("acc no.")
p = input("password.")
account.withdraw(passw)


while is_running:
    print("1. show Balance")
    print("2. deposit")
    print("3. withdraw")
    print("4. Exit")

    choice = input("enter your choice: ")

    if choice == '1':
        account.show_balance()
    elif choice == '2':
        account.deposit()
    elif choice == '3':
        account.withdraw()
    elif choice == '4':
        is_running = False
    else:
        print("invalid choice")