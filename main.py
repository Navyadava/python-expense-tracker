expenses = []

def add_expense():
    amount = float(input("enter expense amount: $"))
    category = input("enter category")
    date = input("enter date (YYYY-MM-DD): ")
    note = input("enter note: ")

expense = {
    "amount": 250.0,
    "category": "Food",
    "date": "2026-08-15",
    "note": "Lunch" 
}

expenses.append(expense)
print("expense added successfully!")

def view_expenses():
    if len(expense) == 0:
        print("no expense found.")
        return

    print("\nsaves expenses")
    print("----------------")

    for expense in expenses:
        print(f"Amount: ${expense['amount']:.2f}")
        print(f"Category: {expense['category']}")
        print(f"Date: {expense['date']}")
        print(f"Note: {expenses['note']}")
        print("--------------")

def calculate_total():
    total = 0

    for expense in expenses:
        total = total + expense["amount"]

    print(f"Total expenses: ${total:.2f}")

while True:
    print("\nExpense Tracker")
    print("----------------")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Show total")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        calculate_total()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Please enter a valid option.")