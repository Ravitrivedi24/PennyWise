from operations import add_transaction, get_transactions

add_transaction(
    25000,
    "expense",
    "Food",
    "Lunch",
    "2026-11-13"
)

print(get_transactions())