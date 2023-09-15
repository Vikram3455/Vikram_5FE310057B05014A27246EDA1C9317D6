class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposited ₹{amount}. New balance: ₹{self.__account_balance}")
        else:
            print("Invalid deposit amount. Amount must be greater than zero.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            print(f"Withdrew ₹{amount}. New balance: ₹{self.__account_balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def display_balance(self):
        print(f"Account Balance for {self.__account_holder_name} (Account #{self.__account_number}): ₹{self.__account_balance}")


# Test the BankAccount class
if __name__ == "__main__":
    # Create a new bank account
    account = BankAccount("123456789", "John Doe", 1000.0)

    # Display initial balance
    account.display_balance()

    # Make some deposits and withdrawals
    account.deposit(500.0)
    account.withdraw(200.0)
    account.withdraw(1500.0)  # This should print an error message

    # Display the final balance
    account.display_balance()