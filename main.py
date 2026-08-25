while True:
    print("\nExpense Tracker")
    print("----------------")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Show total")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print("Add expense selected")

    elif choice == "2":
        print("View expenses selected")

    elif choice == "3":
        print("Show total selected")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Please enter a valid option.")