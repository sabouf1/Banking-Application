# Banking Application in Python using Flask and MySQL

This is a simple banking application written in Python using the Flask framework for web development and MySQL as the database for account information.

## Prerequisites
- Python 3.x installed on your system.
- Flask and mysql-connector-python libraries installed. You can install them using the following commands:
  ```
  pip install Flask
  pip install mysql-connector-python
  ```

## Usage
1. Clone or download this repository to your local machine.

2. Set up the MySQL database:
   - Create a MySQL database with the desired name (e.g., `banking_app_db`).
   - Create a table named `users` with columns `id`, `username`, and `password`.
   - Create a table named `accounts` with columns `id`, `account_number`, `account_holder`, `phone_number`, `address`, `email`, and `balance`.

3. Open the `app.py` script in a text editor.

4. Update the following configurations in the script:
   - Set your secret key for session management: `app.secret_key = 'your_secret_key'`
   - Set your MySQL database connection details in the `connect_to_database` function.

5. Save the changes.

6. Open a terminal or command prompt and navigate to the directory where the script is located.

7. Run the application by executing the following command:
   ```
   python app.py
   ```

8. Access the application in your web browser by visiting `http://localhost:5000`.

## Features
- **Login**: Users can log in using their username and password. User credentials are checked against the MySQL database.
- **Register**: New users can create an account by providing a username and password. Account details are stored in the MySQL database.
- **Open Account**: Logged-in users can open a new bank account by providing account details such as account number, account holder name, phone number, address, and email. The initial account balance is set to 0.
- **Deposit Amount**: Logged-in users can deposit a specified amount into their bank account. The account balance is updated in the MySQL database.
- **Withdraw Amount**: Logged-in users can withdraw a specified amount from their bank account. The account balance is updated in the MySQL database.
- **Balance Enquiry**: Users can check the current balance of their bank account using their account number.
- **List Accounts**: Logged-in users can view a list of all bank accounts in the database.
- **Edit Account**: Logged-in users can edit the details of their bank account, such as account holder name, phone number, address, and email.
- **Close Account**: Logged-in users can close their bank account, and the account details are deleted from the MySQL database.

## Important Notes
- This application is intended for educational purposes and may not include robust security features for a production-ready banking system. Use it responsibly and avoid exposing it to public networks without proper security measures.

## Disclaimer
**USE AT YOUR OWN RISK. THE DEVELOPER IS NOT RESPONSIBLE FOR ANY UNINTENDED CONSEQUENCES CAUSED BY THE USAGE OF THIS APPLICATION.**

## License
This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute the code for any non-malicious purpose.

## Contributions
Contributions to this project are welcome. If you find any issues or want to add enhancements, please submit a pull request.

## Contact
For any questions or inquiries, please contact me.
