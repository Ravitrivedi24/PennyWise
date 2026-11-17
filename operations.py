from storage import load_data, save_data


def add_transaction(amount, transaction_type,
                    category, description, date):

    transactions = load_data()

    # Generate unique ID
    if transactions:
        new_id = max(t["id"] for t in transactions) + 1
    else:
        new_id = 1

    transaction = {
        "id": new_id,
        "type": transaction_type,
        "amount": amount,
        "category": category,
        "description": description,
        "date": date
    }

    transactions.append(transaction)

    save_data(transactions)

def get_transactions():
        return load_data()
def delete_transaction(transaction_id):

    transactions = load_data()

    updated_transactions = []

    deleted = False

    for transaction in transactions:

        if transaction["id"] == transaction_id:
            deleted = True

        else:
            updated_transactions.append(transaction)

    if deleted:
        save_data(updated_transactions)

    return deleted