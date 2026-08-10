from bank import Bank
from exceptions import AccountNotFound, LowBalance

bank = Bank()

while True:
    print("\n===== MINI BANK =====")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Exit")

    choice = input("Enter your choice: ")

    try:
        if choice == "1":
            name = input("Enter name: ")
            balance = float(input("Enter initial balance: "))

            account = bank.create_account(name, balance)

            print("Account Created Successfully")
            print("Account Number:", account.account_no)

        elif choice == "2":
            account_no = int(input("Enter account number: "))
            amount = float(input("Enter deposit amount: "))

            bank.deposit(account_no, amount)

            print("Amount Deposited Successfully")

        elif choice == "3":
            account_no = int(input("Enter account number: "))
            amount = float(input("Enter withdrawal amount: "))

            bank.withdraw(account_no, amount)

            print("Amount Withdrawn Successfully")

        elif choice == "4":
            account_no = int(input("Enter account number: "))

            amount = bank.balance(account_no)

            print("Current Balance:", amount)

        elif choice == "5":
            print("Thank You for Using Mini Bank")
            break

        else:
            print("Invalid Choice")

    except AccountNotFound as e:
        print(e)

    except LowBalance as e:
        print(e)