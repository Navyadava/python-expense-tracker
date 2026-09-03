import sqlite3


DATABASE_NAME = "expenses.db"


def create_table():
    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            date TEXT NOT NULL,
            note TEXT
        )
    """)

    connection.commit()
    connection.close()


def add_expense_to_db(expense):
    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO expenses (amount, category, date, note)
        VALUES (?, ?, ?, ?)
        """,
        (
            expense.amount,
            expense.category,
            expense.date,
            expense.note
        )
    )

    connection.commit()
    connection.close()


def get_all_expenses():
    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM expenses")

    expenses = cursor.fetchall()

    connection.close()

    return expenses