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

def get_total_spending():
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute("SELECT SUM(amount) FROM expenses")

    total = cursor.fetchone()[0]

    connection.close()

    if total is None:
        return 0

    return total

def get_expenses_by_category(category):
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT * FROM expenses
        WHERE LOWER(category) = LOWER(?)
        """,
        (category,)
    )

    expenses = cursor.fetchall()

    connection.close()

    return expenses

def search_expenses_by_note(keyword):
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT * FROM expenses
        WHERE LOWER(note) LIKE LOWER(?)
        """,
        (f"%{keyword}%",)
    )

    expenses = cursor.fetchall()

    connection.close()

    return expenses

def delete_expense_by_id(expense_id):
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM expenses WHERE id = ?",
        (expense_id,)
    )

    deleted = cursor.rowcount > 0

    connection.commit()
    connection.close()

    return deleted

def update_expense_by_id(expense_id, field, new_value):
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    if field == "amount":
        cursor.execute(
            "UPDATE expenses SET amount = ? WHERE id = ?",
            (new_value, expense_id)
        )

    elif field == "note":
        cursor.execute(
            "UPDATE expenses SET note = ? WHERE id = ?",
            (new_value, expense_id)
        )

    else:
        connection.close()
        return False

    updated = cursor.rowcount > 0

    connection.commit()
    connection.close()

    return updated