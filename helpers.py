from datetime import date, datetime

def validate_amount(value):
    try:
        amount = float(value)
    except ValueError:
        raise ValueError("Invalid amount")

    if amount <= 0:
        raise ValueError("Amount must be positive")

    return amount


def get_valid_amount():
    while True:
        user_input = input("Enter amount: $")

        try:
            return validate_amount(user_input)

        except ValueError:
            print("Invalid amount. Please enter a positive number.")


def get_non_empty_text(message):
    while True:
        text = input(message).strip()

        if text:
            return text

        print("This field cannot be blank.")

def get_valid_date():
    today = date.today()

    while True:
        user_input = input(
            f"Enter expense date (YYYY-MM-DD) or press Enter for today [{today}]: "
        ).strip()

        if user_input == "":
            print(f"Date saved: {today}")
            return str(today)

        try:
            valid_date = datetime.strptime(
                user_input,
                "%Y-%m-%d"
            ).date()

            print(f"Date saved: {valid_date}")
            return str(valid_date)

        except ValueError:
            print("Invalid date. Please enter a valid date in YYYY-MM-DD format.")
