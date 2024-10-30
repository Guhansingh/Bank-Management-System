# Bank-Management-System

Here's a `README.md` file for your bank management system program to use on GitHub:

```markdown
# Bank Management System

This project is a simple bank management system created using Python and MySQL. It provides functionalities to manage customer accounts, including opening new accounts, depositing funds, withdrawing funds, checking balance, displaying customer details, and closing accounts.

## Features

1. **Open New Account**: Creates a new bank account for a customer with required details.
2. **Deposit Amount**: Deposits a specified amount into a customer’s account.
3. **Withdraw Amount**: Withdraws a specified amount from a customer’s account.
4. **Balance Enquiry**: Displays the current balance of the customer’s account.
5. **Display Customer Details**: Shows the customer details for a given account.
6. **Close Account**: Deletes a customer’s account and removes their records.

## Requirements

- **Python 3.x**
- **MySQL Server**

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/bank-management-system.git
    ```

2. **Install MySQL Connector for Python**:
    ```bash
    pip install mysql-connector-python
    ```

3. **Setup MySQL Database**:
    - Create a database named `bank_management`.
    - Create the required tables:

      ```sql
      create table account(
          Name varchar(20),
          AccNo varchar(10),
          DOB varchar(10), Address varchar(20),
          ContactNo int,
          OpeningBal int
     );


      CREATE TABLE amount (
          Name VARCHAR(50),
          AccNo VARCHAR(10),
          Balance INT
      );
      ```

4. **Configure Database Connection**:
    - Update the MySQL connection details (username, password, database) in the script if necessary.

## Usage

1. Run the script:
   ```bash
   python bank_management.py
   ```

2. Follow the on-screen options to perform various operations like opening a new account, depositing funds, withdrawing funds, checking balances, displaying customer details, and closing accounts.

## Functions

- `openacc()`: Opens a new account with a unique account number and stores customer details.
- `deposit()`: Adds funds to an existing account.
- `withdraw()`: Deducts funds from an existing account.
- `balance()`: Checks the current balance of an account.
- `display()`: Shows customer details for a specific account.
- `close_acc()`: Deletes a customer's account.

## License

This project is open source and available under the [MIT License](LICENSE).
```

This `README.md` provides an overview of your project, setup instructions, usage guide, and a description of each function.
