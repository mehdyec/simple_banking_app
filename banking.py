class Account:
    def __init__(self, account_number, owner, balance):
        self.owner = owner 
        self.account_number = account_number
        self.balance= balance
    # Deposit
    def deposit(self, amount):
        self.balance = self.balance + amount
    # Withdraw
    def withdraw(self, amount):
        self.balance = self.balance - amount
        
# Action types
DEPOSIT = "DEPOSIT"
WITHDRAW = "WITHDRAW"            

# Create dummy accounts
a1 = Account(1,'Mehdi', 1500)
a2 = Account(2,'John', 5000)
a3 = Account(3,'Sarah', 1000)

accounts = [a1,a2,a3]

# List all accounts and their balances
def list_accounts():
    for account in accounts:
        print(f'Account #{account.account_number} - Owner: {account.owner} - Balance: {account.balance}')


# Close account
def close_account(acc_number):
    # Filter out accounts matching the condition
    current_accounts = filter(lambda account: account.account_number != acc_number, accounts )
    return current_accounts


# Prompt users with the menu
def show_menu():
    print("""Choose an option:
    1. List accounts and their balances
    2. Deposit money to an account
    3. Withdraw money from an account
    4. Open an account
    5. Close an account

    To Exit please press any key that is not in the menu!
    """)


def account_exists(acc_num):
    for account in accounts:
        if account.account_number == acc_num:
            return account 
        return False


def update_balance(acc_num, action_type):
    print(f"How much do you want to {'withdraw' if action_type == WITHDRAW else 'deposit'}: ")
    amount = float(input())
    if action_type == DEPOSIT:
        account.deposit(amount)
        print(f'Account #{acc_num} credited with {amount} successfully!')
    elif action_type == WITHDRAW:
        account.withdraw(amount)
        print(f'Account #{acc_num} debited with {amount} successfully!')
    print("\n")


menu_open = True
while menu_open:
    show_menu()
    response = int(input())
    if response == 1:
        list_accounts()
    elif response == 2:
        print("Please type the account number: ")
        acc_num = int(input())
        # Verify account exists
        account = account_exists(acc_num)
        if not(account):
            print("No such account!")
        else:
            update_balance(acc_num, DEPOSIT )
    elif response == 3:
        print("Please type the account number: ")
        acc_num = int(input())
        # Verify account exists
        account = account_exists(acc_num)
        if not(account):
            print("No such account!")
        else:
            update_balance(acc_num, WITHDRAW)
    elif response == 4:
        name = ''
        while(name == ''):
            print("Please enter your name: ")
            name = input()
        account_number = len(accounts) + 1
        new_account = Account(account_number, name, 0)
        accounts.append(new_account)
        print(f"Success! You account number is #{account_number}")
    elif response == 5:
        print("Please provide the account number: ")
        # Verify account exists
        acc_num = int(input())
        account = account_exists(acc_num)
        if account:
            accounts = close_account(acc_num)
            print(f"Account #{acc_num} was closed successfully. Sorry to see you go")
        else:
            print("No such account")
    else:
        menu_open = False
        print("Bye!")
