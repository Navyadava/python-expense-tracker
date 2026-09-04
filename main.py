import csv
import os
from datetime import date


from expense import Expense
from helpers import get_valid_amount, get_non_empty_text, get_valid_date
from database import create_table, add_expense_to_db, get_all_expenses

FILE_NAME = "expenses.csv"


def create_csv_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Note"])




def load_expenses():
    expenses = []

    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                expenses.append(row)

    except FileNotFoundError:
        pass

    return expenses


def calculate_total(expenses):
    total = 0

    for expense in expenses:
        total += float(expense["Amount"])

    return total


def filter_by_category(expenses, category):
    matching_expenses = []

    for expense in expenses:
        if expense["Category"].lower() == category.lower():
            matching_expenses.append(expense)

    return matching_expenses


def add_expense():
    print("\n--- Add Expense ---")

    expense_date = get_valid_date()

    category = get_non_empty_text("Enter category: ")
    amount = get_valid_amount()
    note = input("Enter note: ").strip()

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)

    expense = Expense(
        amount,
        category,
        expense_date,
        note
    )

    add_expense_to_db(expense)

    print("\nExpense saved successfully!")


def view_expenses():
    print("\n--- Your Expenses ---")

    records = get_all_expenses()

    if not records:
        print("No expenses found.")
        return

    for record in records:
        expense = Expense(
            record[1],
            record[2],
            record[3],
            record[4]
        )

        print(expense)


def show_today_total():
    print("\n--- Today's Total ---")

    today = str(date.today())
    expenses = load_expenses()

    today_expenses = []

    for expense in expenses:
        if expense["Date"] == today:
            today_expenses.append(expense)

    total = calculate_total(today_expenses)

    print(f"Today's total: ${total:.2f}")


def show_all_time_total():
    print("\n--- All-Time Total ---")

    expenses = load_expenses()
    total = calculate_total(expenses)

    print(f"All-time total: ${total:.2f}")


def show_category_expenses():
    print("\n--- Filter By Category ---")

    category = input("Enter category: ").strip()

    if category == "":
        print("Category cannot be blank.")
        return

    expenses = load_expenses()
    matching_expenses = filter_by_category(expenses, category)

    if not matching_expenses:
        print(f"No expenses found for category: {category}")
        return

    print(f"\n{category} expenses:")

    for expense in matching_expenses:
        print(
            f"{expense['Date']} | "
            f"${float(expense['Amount']):.2f} | "
            f"{expense['Note']}"
        )

    total = calculate_total(matching_expenses)

    print(f"\nTotal {category} spending: ${total:.2f}")


def show_menu():
    while True:
        print("\n======================")
        print("    EXPENSE TRACKER")
        print("======================")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Show Today's Total")
        print("4. Show All-Time Total")
        print("5. Filter By Category")
        print("6. Exit")

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
            show_category_expenses()

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please choose 1, 2, 3, 4, 5, or 6.")


if __name__ == "__main__":
    create_table()
    show_menu()
