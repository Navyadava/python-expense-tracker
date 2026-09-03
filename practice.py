class Student:   #class
    def __init__(self, name, course, marks):  #__init__ means constructor
        self.name = name
        self.course = course
        self.marks = marks

    def display_details(self):   #method
        print(f"Name: {self.name}")
        print(f"Course: {self.course}")
        print(f"Marks: {self.marks}")

student1 = Student("Sweety", "Python", 90)   #object
student2 = Student("Maddy", "Java", 90)

student1.display_details()

student2.display_details()









class Book:

    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def apply_discount(self, discount):
        discount_amount = self.price * discount / 100
        new_price = self.price - discount_amount
        return new_price


book1 = Book("Python Basics", "John Smith", 50)

new_price = book1.apply_discount(20)

print()
print("Book:", book1.title)
print("Author:", book1.author)
print(f"Original Price: ${book1.price:.2f}")
print(f"Discounted Price: ${new_price:.2f}")



class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")

    def __str__(self):
        return f"{self.year} {self.brand} {self.model}"

car1 = Car("Toyota", "Camry", 2024)

car1.display_info()
print(car1)


class BankAcount():
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount:.2f}")

        else:
            print("Deposit amount must be positive.")

    def Withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")

        elif amount > self.balance:
            print("Insufficient balance.")

        else:
            self.balance -= amount
            print(f"Withdrawn: ${amount:.2f}")

account1 = BankAcount(500)

account1.deposit(100)
account1.Withdraw(1000)

print(f"Current Balance: ${account1.balance:.2f}")
        

#updating dates:

from datetime import date, datetime, timedelta
today = date.today()
print("Today's date:", today)
print("Formatted date:", today.strftime("%d %B %Y"))
user_date = input("Enter a date (YYYY-MM-DD): ")

try:
    valid_date = datetime.strtime(user_date, "%Y-%M-%D").date()
    print("Valid date:", valid_date)
except ValueError:
    print("Invalid date.")

seven_days_later = today + timedelta(days=7)

print("Seven days from today:", seven_days_later)
