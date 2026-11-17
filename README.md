# PennyWise 💰

### Personal Finance & Expense Tracker

PennyWise is a simple personal finance management application built with Python and Flask. It helps users record their income and expenses, monitor their financial balance, and understand their spending habits through category-wise and monthly summaries.

The project was developed to strengthen Python programming fundamentals while exploring web development.

---

## ✨ Features

- **Transaction Management:** Add income and expense transactions.
- **Financial Dashboard:** View total income, expenses, and available balance.
- **Monthly Summary:** Monitor monthly income, expenses, and balance.
- **Category-wise Breakdown:** Understand where your money is being spent.
- **Search Transactions:** Find transactions using their descriptions.
- **Filtering:** Filter transactions by type and category.
- **Delete Transactions:** Remove unwanted records.
- **Input Validation:** Validate submitted transaction details.
- **Persistent Storage:** Store transaction data locally using JSON.
- **Responsive Interface:** Access the dashboard on desktop and mobile screens.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Flask | Web application framework |
| HTML5 | Webpage structure |
| CSS3 | Styling and responsive design |
| Jinja2 | Dynamic HTML rendering |
| JSON | Local data storage |
| Git & GitHub | Version control and project hosting |

---

## 📁 Project Structure

```text
PennyWise/
│
├── app.py                 # Flask application and routes
├── operations.py          # Transaction operations
├── reports.py             # Financial calculations
├── storage.py             # JSON storage management
│
├── templates/
│   └── index.html         # Main dashboard
│
├── static/
│   └── css/
│       └── style.css      # Stylesheet
│
├── Data/                  # Local transaction data
│
├── requirements.txt       # Python dependencies
├── .gitignore             # Files excluded from Git
├── test_op.py             # Operation tests
└── test_reports.py        # Report calculation tests
```

---

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Ravitrivedi24/PennyWise.git
```

### 2. Navigate to the project directory

```bash
cd PennyWise
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows PowerShell:**

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 6. Configure the Flask secret key

In PowerShell, set a private secret key for your session:

```powershell
$env:FLASK_SECRET_KEY = "your-own-long-random-secret"
```

Use a randomly generated secret and never publish it.

### 7. Run the application

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000/
```

---

## 📊 How It Works

PennyWise follows a modular structure:

- `app.py` handles HTTP requests and connects the frontend to the backend.
- `operations.py` manages adding, retrieving, and deleting transactions.
- `reports.py` calculates financial summaries and category-wise expenses.
- `storage.py` handles reading and writing transaction data in JSON format.
- `index.html` displays the dashboard using Jinja templates.

Transaction amounts are stored as integer paise to avoid common floating-point precision issues in monetary calculations.

---

## 🎯 Learning Objectives

This project helped me practise:

- Python functions and modular programming.
- Lists and dictionaries.
- File handling and JSON.
- Exception handling and input validation.
- Flask routes and HTTP methods.
- HTML forms and Jinja templates.
- CSS styling and responsive layouts.
- Git and GitHub version control.

---

## 🚀 Future Improvements

- Interactive expense charts.
- Edit existing transactions.
- Date-range filtering.
- Export transactions to CSV.
- SQLite database integration.
- User authentication and multiple accounts.

---

## 👨‍💻 Author

**Ravi Trivedi**

GitHub: [@Ravitrivedi24](https://github.com/Ravitrivedi24)

---

*PennyWise — Take control of your money, one transaction at a time.*