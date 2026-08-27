def validate_email(email):
    if "@" in email and "." in email:
        return True
    else:
        return False


email = input("Enter your email: ")

if validate_email(email):
    print("Valid email.")
else:
    print("Invalid email.")