import csv
from datetime import datetime

DATA_FILE = "data.csv"


# 1. Make file if not exits and add Header for file only one time.
# function to create files if it's not exits.
def init_file():
    try:
        with open(DATA_FILE, mode="x", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Type", "Amount", "Category", "Note"])
    except FileExistsError:
        # if file already exits, do nothing
        pass


# 2. show menu items.
def menu():
    print("\n Persnol Expense Tracker")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View All Transactions")
    print("4. Monthly Summary")
    print("5. Exit")


# 3. Function to add transaction like Income or Expense
def add_transaction(transaction_type):
    try:
        # Get user input for details
        amount = float(input("Enter amount: ₹"))
        category = input("Enter category (e.g., Food, Salary, Rent): ")
        note = input("Enter note (optional): ")

        # Get current date.
        date = datetime.now().strftime("%Y-%m-%d")

        # Append the transaction as a new row in the SCV file.
        with open(DATA_FILE, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([date, transaction_type, amount, category, note])
        print("Transaction saved!")
    except Exception as e:
        print(f"Error: {e}")


# 4. View all past transactions.
def view_transactions():
    print("\n All Transaction")
    try:
        with open(DATA_FILE, mode="r") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                print(f"{row[0]} | ₹{row[1]} | {row[2]} | {row[3]} | {row[4]}")
    except FileNotFoundError:
        print("No transaction found yet.")


# 5. Generate a monthly summary
def monthly_summary():
    print("\n Monthly Summary")
    month = input("Enter month (YYYY-MM): ")
    total_income = 0
    total_expense = 0

    try:
        with open(DATA_FILE, mode="r") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if row[0].startswith(month):
                    if row[1] == "Income":
                        total_income = total_income + float(row[2])
                    elif row[1] == "Expense":
                        total_expense = total_expense + float(row[2])

        balance = total_income - total_expense

        # show results
        print(f"Total Income: ₹{total_income}")
        print(f"Total Expense: ₹{total_expense}")
        print(f"Balance : ₹{balance}")

    except FileNotFoundError:
        print("Data file not found.")


# 6. Main programm 
# first make sure data file exits.

init_file()

while True: 
    menu() 
    choice = input("Choose an option: ")

    if choice == '1': 
        add_transaction("Income")
    elif choice == '2':
        add_transaction("Expense")
    elif choice == '3': 
        view_transactions()
    elif choice == '4':
        monthly_summary()
    elif choice == '5':
        print("Existing... stay on budget!")
        break
    else: 
        print("Invaild choice. Please try again.") 