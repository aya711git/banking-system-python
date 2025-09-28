import datetime
from prettytable import PrettyTable

BALANCE = 1000000

# وظيفة لعرض القائمة الرئيسية
def main_menu():
    table = PrettyTable()
    table.field_names = ["Option", "Operation"]
    table.add_row(["1", "Withdraw"])
    table.add_row(["2", "Deposit"])
    table.add_row(["3", "Transfer"])
    table.add_row(["4", "Show Balance"])
    table.add_row(["5", "Exit"])

    print(table)
    choice = input("Enter your choice: ")

    if choice == "1":
        withdraw()

    elif choice == "2":
        deposit()

    elif choice == "3":
        transfer()

    elif choice == "4":
        show_balance()

    elif choice == "5":
        exit()

    else:
        print("Incorrect choice")

# وظيفة لمعالجة عمليات السحب
def withdraw():
    global BALANCE
    amount = float(input("Enter the withdrawal amount: "))
    if amount > BALANCE:
        print("Your balance is not enough")
    else:
        BALANCE -= amount
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Withdrawal successful on {date} for an amount of {amount}")

# وظيفة لمعالجة عمليات الإيداع
def deposit():
    global BALANCE
    amount = float(input("Enter the deposit amount: "))
    BALANCE += amount
    date = datetime.datetime.now()
    print(f"Successfully deposited on {date} for an amount of {amount}")

# وظيفة لمعالجة عمليات التحويلات المصرفية
def transfer():
    global BALANCE
    to_account = input("Enter the account number to transfer to: ")
    amount = float(input("Enter the transfer amount: "))

    if amount > BALANCE:
        print("Your balance is not enough")
    else:
        BALANCE -= amount
        date = datetime.datetime.now()
        print(f"Successfully transferred on {date} an amount of {amount} to account number {to_account}")

# وظيفة لعرض الرصيد
def show_balance():
    print(f"Your current balance is {BALANCE}")

# بدء تشغيل البرنامج
main_menu()

