import csv
import os
from datetime import date

FILE_NAME = "expenses.csv"

def create_csv_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline = "") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Note"])


def add_expense():
    print("\n---Add Expense ---")

    expense_date = input(
        "Enter date (YYYY-MM-DD) or press Enter for today: "
    )
    if expense_date == "":
        expense_date = str(date.today())

    category = input("enter category")
    amount = float(input("enter expense amount: $"))
    note = input("enter note: ")

    with open(FILE_NAME, "a", newline = "") as file:
        writer = csv.writer(file)

        writer.writerow([
            expense_date,
            category,
            amount,
            note
        ])

print("expense added successfully!")

def view_expenses():
    print("\n----Your expenses---")

    with open(FILE_NAME, "r")as file:
        reader = csv.DictReader(file)

        found = False

        for expenses in reader:
            found = True

        print(
            f"Date: {expenses['Date']}|"
            f"Category: {expenses['Category']}|"
            f"Amount: ${float(expenses['Amount']):.2f}|"
            f"Note: {expenses['Note']}|"
        )

    if not found:
        print("No expenses found.")

def show_menu():
    while True:
        print("\n-----------")
        print("     Expense Tracker")
        print("---------------")
        print("1. Add expense")
        print("2. View expenses")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

create_csv_file()
show_menu()