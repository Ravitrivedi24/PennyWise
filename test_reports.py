from operations import get_transactions

from reports import (
    calculate_total_income,
    calculate_total_expenses,
    calculate_balance,
    category_summary,
    monthly_summary
)


transactions = get_transactions()


print("Total Income:", calculate_total_income(transactions) / 100)

print("Total Expenses:", calculate_total_expenses(transactions) / 100)

print("Balance:", calculate_balance(transactions) / 100)

print("Category Summary:", category_summary(transactions))

print("Monthly Summary:", monthly_summary(transactions))