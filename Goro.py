import json
import os
from datetime import datetime

# 📁 File to save expenses
DATA_FILE = "expenses.json"

# 🧾 Load existing data or initialize empty list
def load_expenses():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return []

# 💾 Save data to file
def save_expenses(expenses):
    with open(DATA_FILE, 'w') as file:
        json.dump(expenses, file, indent=4)

# ➕ Add a new expense
def add_expense():
    try:
        amount = float(input("Enter amount: ₹"))
    except ValueError:
        print("❌ Invalid amount. Please enter a number.")
        return

    category = input("Enter category (food, travel, etc): ").strip()
    note = input("Note (optional): ").strip()
    date = datetime.now().strftime('%Y-%m-%d')

    expense = {
        "amount": amount,
        "category": category,
        "note": note,
        "date": date
    }

    expenses = load_expenses()
    expenses.append(expense)
    save_expenses(expenses)
    print("✅ Expense saved!")

# 📋 View all expenses
def view_expenses():
    expenses = load_expenses()
    if not expenses:
        print("No expenses found.")
        return

    for i, e in enumerate(expenses, 1):
        print(f"{i}. ₹{e['amount']} | {e['category']} | {e['note']} | {e['date']}")

# 📅 Filter by date or month
def filter_by_date():
    choice = input("Filter by (d)ate or (m)onth? ").lower()
    target = input("Enter date (YYYY-MM-DD) or month (YYYY-MM): ").strip()

    expenses = load_expenses()
    filtered = [e for e in expenses if e['date'].startswith(target)]

    if not filtered:
        print("No expenses found for that date/month.")
        return

    total = 0
    for i, e in enumerate(filtered, 1):
        print(f"{i}. ₹{e['amount']} | {e['category']} | {e['note']} | {e['date']}")
        total += e['amount']

    print(f"\n🔢 Total: ₹{total}")

# 📊 Show category-wise summary
def show_category_summary():
    expenses = load_expenses()
    if not expenses:
        print("No expenses found.")
        return

    summary = {}
    total = 0

    for e in expenses:
        cat = e['category']
        amt = e['amount']
        summary[cat] = summary.get(cat, 0) + amt
        total += amt

    print("\n📊 Expenses by Category:")
    for cat, amt in summary.items():
        print(f"{cat}: ₹{amt}")
    print(f"\n🔢 Total Spent: ₹{total}")

# 🧠 Main menu
def menu():
    while True:
        print("\n===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Filter by Date/Month")
        print("4. Exit")
        print("5. Show Category Summary")
        choice = input("Choose an option: ").strip()

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            filter_by_date()
        elif choice == '4':
            print("👋 Exiting. Save money!")
            break
        elif choice == '5':
            show_category_summary()
        else:
            print("❌ Invalid choice. Try again.")

# 🚀 Run the app
menu()
