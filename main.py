import csv
import os
from datetime import date


FILE_NAME = "expenses.csv"


def create_csv_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Note"])


def get_valid_amount():
    while True:
        try:
            amount = float(input("Enter amount: $"))

            if amount <= 0:
                print("Invalid amount. Please enter a positive number.")
            else:
                return amount

        except ValueError:
            print("Invalid amount. Please enter a positive number.")


def get_valid_category():
    while True:
        category = input("Enter category: ").strip()

        if category == "":
            print("Category cannot be blank.")
        else:
            return category


def add_expense():
    print("\n--- Add Expense ---")

    expense_date = input(
        "Enter date (YYYY-MM-DD) or press Enter for today: "
    ).strip()

    if expense_date == "":
        expense_date = str(date.today())

    category = get_valid_category()
    amount = get_valid_amount()
    note = input("Enter note: ").strip()

    create_csv_file()

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            expense_date,
            category,
            f"{amount:.2f}",
            note
        ])

    print("\nExpense saved successfully!")


def view_expenses():
    print("\n--- Your Expenses ---")

    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.DictReader(file)

            found = False

            for expense in reader:
                found = True

                print(
                    f"Date: {expense['Date']} | "
                    f"Category: {expense['Category']} | "
                    f"Amount: ${float(expense['Amount']):.2f} | "
                    f"Note: {expense['Note']}"
                )

            if not found:
                print("No expenses found.")

    except FileNotFoundError:
        print("No expenses found yet.")


def show_today_total():
    print("\n--- Today's Total ---")

    today = str(date.today())
    total = 0

    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.DictReader(file)

            for expense in reader:
                if expense["Date"] == today:
                    total += float(expense["Amount"])

        print(f"Today's total: ${total:.2f}")

    except FileNotFoundError:
        print("No expenses found yet.")


def show_all_time_total():
    print("\n--- All-Time Total ---")

    total = 0

    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.DictReader(file)

            for expense in reader:
                total += float(expense["Amount"])

        print(f"All-time total: ${total:.2f}")

    except FileNotFoundError:
        print("No expenses found yet.")


def show_menu():
    while True:
        print("\n======================")
        print("    EXPENSE TRACKER")
        print("======================")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Show Today's Total")
        print("4. Show All-Time Total")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            show_today_total()

        elif choice == "4":
            show_all_time_total()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please choose 1, 2, 3, 4, or 5.")


create_csv_file()
show_menu()