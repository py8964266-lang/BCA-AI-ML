# Bank Account Management System

A Python-based banking system that simulates real-world bank account operations, built to demonstrate core Object-Oriented Programming (OOP) principles.

**  About

This project models a simple banking system where users can create accounts, deposit/withdraw money, and view account details — while keeping sensitive data like account balance protected using encapsulation.

** Features

- Create a bank account with holder details (name, account number, mobile number, address)
- View account holder details
- Check account balance
- Deposit money (with validation)
- Withdraw money (with balance and validation checks)
- Two specialized account types: **Savings Account** (with interest) and **Current Account** (with overdraft)

**  OOP Concepts Used

- **Encapsulation** — Account balance (`__balance`) is kept private and can only be accessed through class methods, protecting it from direct external modification.
- **Inheritance** — `SavingAccount` and `CurrentAccount` inherit common functionality (details, deposit, withdraw) from the base `BankAccount` class, avoiding code duplication.

** Tech Stack

- Python 3

** How to Run

1. Clone this repository:
```bash
   
```
2. Run the file:
```bash
   python bank_account_system.py
```

** Future Improvements

- Add a menu-driven interface for user interaction
- Add polymorphism by overriding methods differently in `SavingAccount` and `CurrentAccount`
- Add transaction history tracking
- Persist data using file handling or a database

** Author

**Piyush Yadav**
BCA Student, Galgotias University | Aspiring AI/ML Engineer
