import random


class Bank:
    name = "DBBL"

    def __init__(self):
        self.accounts = []

    def create_account(self, name, email, address, account_type):
        account = Account(name, email, address, account_type)
        self.accounts.append(account)
        print("\n----Account created successfully-----\n")
        print(f"Account Number: {account._Account__account_number}")
        print(f"Account Name: {account.name}")
        print(f"Account Type: {account.account_type}\n")
        return account

    def delete_account(self, account_number):
        for account in self.accounts:
            if account.__account_number == account_number:
                self.accounts.remove(account)
            else:
                print("Account not found")
                break

    def __repr__(self):
        print(f"Bank Name: {self.name}")
        for account in self.accounts:
            print(account)

        return ""

    def total_balance(self):
        total_balance = 0
        for account in self.accounts:
            total_balance += account._Account__balance
        print(f"Total available balance in the bank: ${total_balance}")

    def total_loan(self):
        total_loan = 0
        for account in self.accounts:
            total_loan += account.loan
        print(f"Total loan in the bank: {total_loan}")


class Account:
    def __init__(self, name, email, address, account_type):
        self.name = name
        self.__email = email
        self.address = address
        self.__balance = 0
        self.account_type = account_type
        self.transaction_history = {}
        self.can_take_loan = 2
        self.isBankrupt = False
        self.loan = 0
        self.__account_number = self.generate_account_number()

    def generate_account_number(self):
        account_number = random.randint(1000, 9999)
        return account_number

    def deposit(self, amount):
        self.__balance += amount
        self.transaction_history["Deposit"] = amount
        print(f'\nYou have deposited ${amount} successfully\n')

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            self.transaction_history["Withdraw"] = amount
            print(f'\nYou have withdrawn ${amount} successfully\n')
        else:
            print("Withdrawal amount exceeded")

    def transfer(self, amount, account_number):
        if amount <= self.__balance:
            self.__balance -= amount
            self.transaction_history[account_number] = amount
            print(f'\nYou have transferred ${amount} to account number {account_number} successfully\n')

        else:
            print("Account does not exist")

    def view_history(self):
        print("\n-----Transaction History----\n")
        print(self.transaction_history)

    def check_balance(self):
        print(f"Your current balance is: ${self.__balance}")

    def take_loan(self, amount):
        if self.can_take_loan > 0 and admin.isLoanActive:
            if amount > 0:
                self.__balance += amount
                self.can_take_loan -= 1
                self.loan += amount
                self.transaction_history["Loan"] = amount
                print(f'\nYou have taken a loan of ${amount} successfully\n')
            else:
                print("Invalid loan amount")
        else:
            print("You have reached the maximum number of loans")

    def __repr__(self):
        return f"Account Number: {self.__account_number}\nAccount Name: {self.name}\nAccount Type: {self.account_type} \nBalance: {self.__balance}\nEmail: {self.__email}\nAddress: {self.address}\n"


class Admin:
    def __init__(self):
        self.isLoanActive = True

    def create_account(self, name, email, address, account_type):
        account = Account(name, email, address, account_type)
        return account

    def make_bankrupt(self, account_number):
        for account in bank.accounts:
            if account.__account_number == account_number:
                account.isBankrupt = True

    def enable_loan(self, enable):
        self.isLoanActive = enable

    def delete_account(self, account_number):
        bank.delete_account(account_number)

    def get_total_balance(self):
        bank.total_balance()

    def get_loan(self):
        bank.total_loan()

    def user_list(self):
        if len(bank.accounts) == 0:
            print("No user found")
        else:
            for account in bank.accounts:
                print(f'Name: {account.name} \nAccount Number: {account._Account__account_number}\n')


bank = Bank()
admin = Admin()
current_user = None

while True:
    if current_user is None:
        print(f'Welcome to {bank.name} Bank')
        print("L. Login")
        print("R. Register")
        print("A. Admin Login")
        choice = input("\nEnter your choice: ")
        if choice == "R":
            name = input("Name: ")
            email = input("Email: ")
            address = input("Address: ")
            account_type = input("Account Type savings or current: ")
            account = bank.create_account(name, email, address, account_type)
            current_user = account
        elif choice == "L":
            account_number = int(input("Account Number: "))
            for account in bank.accounts:
                if account._Account__account_number == account_number:
                    current_user = account
                    break
            else:
                print("Account not found")
        elif choice == "A":
            ch = input("Enter Admin Password: ")
            print("----Admin Login Successful----")
            admin_mode = True
            while admin_mode is True:
                print("1. Create Account")
                print("2. Delete Account")
                print("3. View Total Balance")
                print("4. View Total Loan")
                print("5. Loan Feature on/off")
                print("6. View User List")
                print("7. Logout")
                op = input("\nChoose an option: ")
                if op == "1":
                    name = input("Name: ")
                    email = input("Email: ")
                    address = input("Address: ")
                    account_type = input("Account Type savings or current: ")
                    account = bank.create_account(name, email, address, account_type)
                elif op == "2":
                    account_number = int(input("Enter the account number to delete: "))
                    admin.delete_account(account_number)
                elif op == "3":
                    admin.get_total_balance()
                elif op == "4":
                    admin.get_loan()
                elif op == "5":
                    enable = input("on/off: ")
                    if enable == "on":
                        admin.enable_loan(True)
                    else:
                        admin.enable_loan(False)
                elif op == "6":
                    admin.user_list()
                elif op == "7":
                    admin_mode = False
                else:
                    print("Invalid option")
                    break

    else:
        print(f'Welcome {current_user.name}')
        print("1.Deposit")
        print("2.Withdraw")
        print("3.Transfer")
        print("4.View Balance")
        print("5.Take Loan")
        print("6.View Transaction History")
        print("7.Logout")
        op = input("\nChoose an option: ")
        if op == "1":
            amount = int(input("Enter the amount to deposit: "))
            current_user.deposit(amount)
        elif op == "2":
            amount = int(input("Enter the amount to withdraw: "))
            current_user.withdraw(amount)
        elif op == "3":
            amount = int(input("Enter the amount to transfer: "))
            account_number = int(input("Enter the account number to transfer: "))
            current_user.transfer(amount, account_number)
        elif op == "4":
            current_user.check_balance()
        elif op == "5":
            amount = int(input("Enter the amount to take loan: "))
            current_user.take_loan(amount)
        elif op == "6":
            current_user.view_history()
        elif op == "7":
            current_user = None
        else:
            print("Invalid option")
            break
