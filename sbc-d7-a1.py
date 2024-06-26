from random import randint

accounts = {}

def create_account():
    name = input("Enter your name: ")
    account_id = randint(100, 999)
    accounts[account_id] = {'name': name, 'balance': 0}
    print(f"Account created successfully! Account ID is: {account_id}")

def delete_account():
    account_id = int(input("Enter account ID to delete: "))
    if account_id in accounts:
        del accounts[account_id]
        print(f"Account with ID {account_id} has been deleted successfully")
    else:
        print("Account not found")

def show_balance(account_id):
    if account_id in accounts:
        print(f"Your current balance is P{accounts[account_id]['balance']:.2f}")
    else:
        print("Account not found")

def deposit(account_id):
    amount = float(input("Enter amount to deposit: "))
    if amount < 0:
        print("Input a valid amount")
    else:
        accounts[account_id]['balance'] += amount
        print("Deposit successful")

def withdraw(account_id):
    amount = float(input("Enter amount to withdraw: "))
    if amount < 0:
        print("Amount must be greater than 0")
    elif amount > accounts[account_id]['balance']:
        print("Insufficient balance")
    else:
        accounts[account_id]['balance'] -= amount
        print("Withdrawal successful")

while True:
    print("My Bank System")
    print("1. Create Account")
    print("2. Balance")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Delete Account")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")
    if choice == '1':
        create_account()
    elif choice == '2':
        account_id = int(input("Enter account ID: "))
        show_balance(account_id)
    elif choice == '3':
        account_id = int(input("Enter account ID: "))
        deposit(account_id)
    elif choice == '4':
        account_id = int(input("Enter account ID: "))
        withdraw(account_id)
    elif choice == '5':
        delete_account()
    elif choice == '6':
        break
    else:
        print("Invalid choice. Please select a valid option.")
