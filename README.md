Backend-Daily
Banking API System
Overview

This project involves building a simple RESTful API for a banking system using Python and Flask. The API will enable users to create, update, delete, and view account information, as well as perform transactions like deposits and withdrawals. The backend will be powered by an SQL database to store account and transaction data.
Objectives

    Create Accounts: Allow users to create new bank accounts with details like name, email, and initial balance.
    Update Account Information: Users should be able to update account information, such as name, email, and contact details.
    Delete Accounts: Users can delete their account if they no longer need it.
    Transactions: Enable users to deposit and withdraw funds.
    Account Balance: Users can view their balance and transaction history.

API Endpoints

Below are example endpoints to get started:

    POST /accounts: Creates a new account.
        Hint: Use request.get_json() to retrieve data from the request.

    GET /accounts/<account_id>: Retrieves information about a specific account.
        Hint: Use query parameters to filter and GET to retrieve information.

    PUT /accounts/<account_id>: Updates account information.
        Hint: Use SQL UPDATE carefully to avoid overwriting data.

    DELETE /accounts/<account_id>: Deletes an account.
        Hint: Consider adding a confirmation step to avoid accidental deletions.

    POST /transactions/deposit: Adds funds to an account.
        Hint: Validate that the account exists before adding funds.

    POST /transactions/withdraw: Withdraws funds from an account.
        Hint: Check that the balance does not fall below zero.

Requirements

    Flask for the API framework.
    SQLite or MySQL for the SQL database.
    SQLAlchemy (optional) for ORM.

Steps & Hints

    Setup: Initialize a Flask app and install packages (flask, flask_sqlalchemy, and sqlite3 if using SQLite).

    Database Models:
        Define two primary tables: Account and Transaction.
        Account table might include columns like id, name, email, balance.
        Transaction table can track transaction_id, account_id, amount, and type (deposit or withdrawal).

    Database Operations:
        Use SQLAlchemy (or raw SQL) to create functions for creating, reading, updating, and deleting records.

    Endpoints and Routes:
        Create routes for each endpoint and map them to specific controller functions.
        Implement error handling (e.g., account not found, insufficient balance).

    Transaction Logic:
        Handle deposits and withdrawals correctly.
        Hint: Use commit() only after ensuring the transaction meets requirements (e.g., no negative balances).

    Testing:
        Test each endpoint individually with tools like Postman or Insomnia.
        Validate error handling with edge cases (e.g., withdrawing more than the available balance).

    Documentation:
        Document each endpoint and expected parameters, using Swagger or markdown files.

Extensions (Optional)

Once completed, consider adding:

    Authorization: Implement token-based authentication to secure account data.
    Transaction History Pagination: Allow users to paginate transaction history.
    Transaction Rollback: Implement rollback functionality to ensure data consistency in case of errors.

Extra Tips

    Validate user input, especially for sensitive actions like withdrawals.
    SQLAlchemy ORM: Try using ORM instead of raw SQL to simplify database operations and prevent SQL injection.
