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