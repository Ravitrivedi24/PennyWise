
import json
import os

FILE_PATH = "data/transactions.json"


def load_data():

    # Check whether the JSON file exists
    if not os.path.exists(FILE_PATH):
        return []

    try:
        with open(FILE_PATH, "r", encoding="utf-8") as file:
            transactions = json.load(file)

        # Ensure the stored data is a list
        if not isinstance(transactions, list):
            raise ValueError("Transaction data must be a list.")

        return transactions

    except json.JSONDecodeError as error:
        raise ValueError(
            "Your transactions.json file contains invalid JSON. "
            "Please restore it from a backup or repair the file."
        ) from error


def save_data(transactions):

    # Create the data folder if it doesn't exist
    os.makedirs("data", exist_ok=True)

    # Write to a temporary file first
    temp_path = FILE_PATH + ".tmp"

    with open(temp_path, "w", encoding="utf-8") as file:
        json.dump(transactions, file, indent=4)

    # Replace the original file after writing successfully
    os.replace(temp_path, FILE_PATH)
