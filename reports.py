def calculate_total_income(transactions):

    total = 0

    for transaction in transactions:

        if transaction["type"] == "income":
            total += transaction["amount"]

    return total
def calculate_total_expenses(transactions):

    total = 0

    for transaction in transactions:

        if transaction["type"] == "expense":
            total += transaction["amount"]

    return total
def calculate_balance(transactions):

    income = calculate_total_income(transactions)

    expenses = calculate_total_expenses(transactions)

    return income - expenses
def category_summary(transactions):

    summary = {}

    for transaction in transactions:

        if transaction["type"] == "expense":

            category = transaction["category"]

            amount = transaction["amount"]

            if category in summary:
                summary[category] += amount

            else:
                summary[category] = amount

    return summary
from datetime import datetime


def monthly_summary(transactions, year=None, month=None):

    if year is None or month is None:
        today = datetime.now()
        year = today.year
        month = today.month

    income = 0
    expenses = 0

    for transaction in transactions:

        transaction_date = datetime.strptime(
            transaction["date"], "%Y-%m-%d"
        )

        if transaction_date.year == year and transaction_date.month == month:

            if transaction["type"] == "income":
                income += transaction["amount"]

            elif transaction["type"] == "expense":
                expenses += transaction["amount"]

    return {
        "income": income,
        "expenses": expenses,
        "balance": income - expenses
    }