import csv
import os
from datetime import date


from expense import Expense
from helpers import get_valid_amount, get_non_empty_text, get_valid_date
from database import (
    create_table, 
    add_expense_to_db, 
    get_all_expenses,
    get_total_spending,
    get_expenses_by_category,
    search_expenses_by_note,
    delete_expense_by_id,
    update_expense_by_id
)

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
    print("\n--- All Expenses ---")

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

        print(f"ID: {record[0]} | {expense}")


def show_total_spending():

    total = get_total_spending()

    print("\n--- Total Spending ---")
    print(f"Total spending: ${total:.2f}")


def show_all_time_total():
    print("\n--- All-Time Total ---")

    expenses = load_expenses()
    total = calculate_total(expenses)

    print(f"All-time total: ${total:.2f}")


def show_category_filter():
    category = get_non_empty_text("Enter category: ")

    records = get_expenses_by_category(category)

    if not records:
        print("No expenses found for this category.")
        return

    print(f"\n--- {category} Expenses ---")

    for record in records:
        expense = Expense(
            record[1],
            record[2],
            record[3],
            record[4]
        )

        print(f"ID: {record[0]} | {expense}")

def show_note_search():
    keyword = get_non_empty_text("Enter note keyword: ")

    records = search_expenses_by_note(keyword)

    if not records:
        print("No matching expenses found.")
        return

    print("\n--- Search Results ---")

    for record in records:
        expense = Expense(
            record[1],
            record[2],
            record[3],
            record[4]
        )

        print(f"ID: {record[0]} | {expense}")

def delete_expense():
    view_expenses()

    try:
        expense_id = int(input("\nEnter expense ID to delete: "))
    except ValueError:
        print("Invalid ID.")
        return

    confirm = input("Are you sure? (yes/no): ").strip().lower()

    if confirm != "yes":
        print("Delete cancelled.")
        return

    if delete_expense_by_id(expense_id):
        print("Expense deleted successfully.")
    else:
        print("Expense ID not found.")

def update_expense():
    view_expenses()

    try:
        expense_id = int(input("\nEnter expense ID to update: "))
    except ValueError:
        print("Invalid ID.")
        return

    print("\nWhat do you want to update?")
    print("1. Amount")
    print("2. Note")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        new_amount = get_valid_amount()

        if update_expense_by_id(
            expense_id,
            "amount",
            new_amount
        ):
            print("Amount updated successfully.")
        else:
            print("Expense ID not found.")

    elif choice == "2":
        new_note = get_non_empty_text("Enter new note: ")

        if update_expense_by_id(
            expense_id,
            "note",
            new_note
        ):
            print("Note updated successfully.")
        else:
            print("Expense ID not found.")

    else:
        print("Invalid choice.")


def show_menu():
    while True:
        print("\n======================")
        print("    EXPENSE TRACKER")
        print("======================")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Show Total Spending")
        print("4. Filter By Category")
        print("5. Search By Note")
        print("6. Update Expense")
        print("7. Delete Expense")
        print("8. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            show_total_spending()

        elif choice == "4":
            show_category_filter()

        elif choice == "5":
            show_note_search()

        elif choice == "6":
            update_expense()

        elif choice == "7":
            delete_expense()

        elif choice == "8":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please choose 1 through 8.")


if __name__ == "__main__":
    create_table()
    show_menu()
