
from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    flash
)
from datetime import datetime
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP

from operations import (
    add_transaction,
    get_transactions,
    delete_transaction
)

from reports import (
    calculate_total_income,
    calculate_total_expenses,
    calculate_balance,
    category_summary,
    monthly_summary
)

app = Flask(__name__)
import os

app.secret_key = os.environ.get("FLASK_SECRET_KEY")




@app.route("/")
def home():

    # 1. Get all transactions
    all_transactions = get_transactions()

    # 2. Get filter values from URL
    search_query = request.args.get("q", "").strip()
    selected_type = request.args.get("type", "").strip()
    selected_category = request.args.get("category", "").strip()

    # 3. Start with all transactions
    filtered_transactions = all_transactions

    # 4. Search by description
    if search_query:
        filtered_transactions = [
            t for t in filtered_transactions
            if search_query.casefold() in t["description"].casefold()
        ]

    # 5. Filter by transaction type
    if selected_type in ["income", "expense"]:
        filtered_transactions = [
            t for t in filtered_transactions
            if t["type"] == selected_type
        ]

    # 6. Filter by category
    if selected_category:
        filtered_transactions = [
            t for t in filtered_transactions
            if t["category"] == selected_category
        ]

    # 7. Get available categories
    available_categories = sorted({
        t["category"] for t in all_transactions
    })

    # 8. Calculate summaries using ALL transactions
    total_income = calculate_total_income(all_transactions)
    total_expenses = calculate_total_expenses(all_transactions)
    balance = calculate_balance(all_transactions)
    categories = category_summary(all_transactions)
    monthly = monthly_summary(all_transactions)

    # 9. Send information to HTML
    return render_template(
        "index.html",
        name="Ravi",
        transactions=filtered_transactions,
        total_income=total_income,
        total_expenses=total_expenses,
        balance=balance,
        categories=categories,
        monthly=monthly,
        search_query=search_query,
        selected_type=selected_type,
        selected_category=selected_category,
        available_categories=available_categories
    )




@app.route("/add", methods=["POST"])
def add():

    # 1. Retrieve form values
    transaction_type = request.form.get("type", "").strip()
    amount_input = request.form.get("amount", "").strip()
    category = request.form.get("category", "").strip()
    description = request.form.get("description", "").strip()
    date = request.form.get("date", "").strip()

    # 2. Validate transaction type
    if transaction_type not in ["income", "expense"]:
        flash("Invalid transaction type.", "error")
        return redirect(url_for("home"))

    # 3. Validate category
    allowed_categories = [
        "Food",
        "Travel",
        "Shopping",
        "Education",
        "Entertainment",
        "Pocket Money",
        "Salary",
        "Other"
    ]

    if category not in allowed_categories:
        flash("Invalid category.", "error")
        return redirect(url_for("home"))

    # 4. Validate description
    if not description or len(description) > 100:
        flash("Description must contain 1–100 characters.", "error")
        return redirect(url_for("home"))

    # 5. Validate amount
    try:
        amount_rupees = Decimal(amount_input)

        if not amount_rupees.is_finite() or amount_rupees <= 0:
            raise ValueError

        amount_paise = int(
            (amount_rupees * 100).quantize(
                Decimal("1"),
                rounding=ROUND_HALF_UP
            )
        )

        if amount_paise <= 0:
            raise ValueError

    except (InvalidOperation, ValueError):
        flash("Please enter a valid positive amount.", "error")
        return redirect(url_for("home"))

    # 6. Validate date
    try:
        datetime.strptime(date, "%Y-%m-%d")

    except ValueError:
        flash("Please enter a valid date.", "error")
        return redirect(url_for("home"))

    # 7. Save transaction only after all validations pass
    add_transaction(
        amount_paise,
        transaction_type,
        category,
        description,
        date
    )

    flash("Transaction added successfully!", "success")

    return redirect(url_for("home"))



@app.route("/about")
def about():
    return "PennyWise is a personal expense tracker."


@app.route("/delete/<int:transaction_id>", methods=["POST"])
def delete(transaction_id):

    deleted = delete_transaction(transaction_id)

    if deleted:
        flash("Transaction deleted successfully.", "success")
    else:
        flash("Transaction not found.", "error")

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
