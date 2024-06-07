`README.md`
```markdown
 Banking Application

This project is a Python-based banking application that supports different types of bank accounts with specific rules and constraints. The application demonstrates the use of object-oriented programming principles such as inheritance, polymorphism, and encapsulation.

 Project Structure

The project is organized as follows:

```
project_directory/
├── account.py
├── savings_account.py
├── current_account.py
├── childrens_account.py
├── student_account.py
├── main.py
└── tests/
    ├── test_account.py
    ├── test_savings_account.py
    ├── test_current_account.py
    ├── test_childrens_account.py
    └── test_student_account.py
```

 Account Types

1. Savings Account:
    - Gains interest of 0.5% per deposit.
    - Withdrawal limit of 700,000.
    
2. Current Account:
    - No restrictions on deposits or withdrawals.
    
3. Children's Account:
    - Gains interest of 0.7% per deposit.
    - Withdrawals are not allowed.
    
4. Student Account:
    - Withdrawal limit of 2,000.
    - Deposit limit of 50,000 per deposit.

 Running the Application

 Prerequisites

- Python 3.x must be installed on your system.

 Running the Main Script

1. Open a terminal or command prompt.
2. Navigate to the project directory:

    ```bash
    cd path/to/project_directory
    ```

3. Run the `main.py` script:

    ```bash
    python main.py
    ```

 Running the Tests

1. Open a terminal or command prompt.
2. Navigate to the project directory:

    ```bash
    cd path/to/project_directory
    ```

3. Run the tests using the `unittest` module:

    ```bash
    python -m unittest discover -s tests
    ```

 Code Overview

 `account.py`

Contains the base `Account` class with common functionalities such as deposit, withdraw, and balance checking.

 `savings_account.py`

Contains the `SavingsAccount` class which inherits from `Account` and adds interest calculation on deposits and a withdrawal limit.

 `current_account.py`

Contains the `CurrentAccount` class which inherits from `Account` with no additional restrictions.

 `childrens_account.py`

Contains the `ChildrensAccount` class which inherits from `Account`, adds interest calculation on deposits, and disallows withdrawals.

 `student_account.py`

Contains the `StudentAccount` class which inherits from `Account` and imposes deposit and withdrawal limits.

 `main.py`

Demonstrates example usage of the different account types.

 `tests`

Contains unit tests for each account type to ensure the application behaves as expected.

- `test_account.py`: Tests for the base `Account` class.
- `test_savings_account.py`: Tests for the `SavingsAccount` class.
- `test_current_account.py`: Tests for the `CurrentAccount` class.
- `test_childrens_account.py`: Tests for the `ChildrensAccount` class.
- `test_student_account.py`: Tests for the `StudentAccount` class.

 Acknowledgements

This project was developed as an example to demonstrate object-oriented programming principles in Python.
```

This `README.md` file provides an overview of the project, instructions for running the application and tests, a brief description of each file, and other relevant information.
