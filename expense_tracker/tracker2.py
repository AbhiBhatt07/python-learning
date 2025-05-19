import json
from datetime import datetime
import os

# File to store data
DATA_FILE = "data.json"


# 🔹 Initialize the data file if not already created
def init_file():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as file:
            json.dump([], file)  # Start with an empty list


# 🔹 Read data from the JSON file
def read_data():
    with open(DATA_FILE, "r") as file:
        return json.load(file)


# 🔹 Write data to the JSON file
def write_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)


# 🔹 Add a new income or expense
def add_transaction(transaction_type):
    try:
        amount = float(input("Enter amount: ₹"))
        category = input("Enter category (e.g., Food, Salary): ")
        note = input("Enter note (optional): ")
        date = datetime.now().strftime("%Y-%m-%d")

        new_entry = {
            "date": date,
            "type": transaction_type,
            "amount": amount,
            "category": category,
            "note": note,
        }

        data = read_data()
        data.append(new_entry)
        write_data(data)

        print("✅ Transaction saved!")

    except Exception as e:
        print(f"❌ Error: {e}")


# 🔹 Show all transactions
def view_transactions():
    print("\n--- All Transactions ---")
    try:
        data = read_data()
        if not data:
            print("No transactions found.")
        for entry in data:
            print(
                f"📅 {entry['date']} | {entry['type']} | ₹{entry['amount']} | {entry['category']} | {entry['note']}"
            )
    except FileNotFoundError:
        print("❌ Data file not found.")


# 🔹 Monthly summary view
def monthly_summary():
    print("\n--- Monthly Summary ---")
    month = input("Enter month (YYYY-MM): ")
    try:
        data = read_data()

        total_income = sum(
            item["amount"]
            for item in data
            if item["type"] == "Income" and item["date"].startswith(month)
        )
        total_expense = sum(
            item["amount"]
            for item in data
            if item["type"] == "Expense" and item["date"].startswith(month)
        )
        balance = total_income - total_expense

        print(f"📈 Total Income: ₹{total_income}")
        print(f"📉 Total Expense: ₹{total_expense}")
        print(f"💰 Balance: ₹{balance}")

    except FileNotFoundError:
        print("❌ Data file not found.")


# 🔹 Show the menu
def menu():
    print("\n--- Personal Expense Tracker ---")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View All Transactions")
    print("4. Monthly Summary")
    print("5. Exit")


# 🔹 Main program loop
if __name__ == "__main__":
    init_file()
    while True:
        menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_transaction("Income")
        elif choice == "2":
            add_transaction("Expense")
        elif choice == "3":
            view_transactions()
        elif choice == "4":
            monthly_summary()
        elif choice == "5":
            print("👋 Exiting... Stay on budget!")
            break
        else:
            print("❌ Invalid choice. Please try again.")
