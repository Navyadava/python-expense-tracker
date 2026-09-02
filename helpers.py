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