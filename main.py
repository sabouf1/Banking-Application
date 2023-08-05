from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set your secret key for session management

# Connect to the MySQL database
def connect_to_database():
    try:
        db = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='EL#u9yzOewh+69',
            database='bank'
        )
        return db
    except mysql.connector.Error as error:
        print('Error connecting to MySQL database:', error)

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        db = connect_to_database()
        if db is not None:
            cursor = db.cursor()
            query = 'SELECT * FROM users WHERE username = %s AND password = %s'
            values = (username, password)
            cursor.execute(query, values)
            user = cursor.fetchone()
            db.close()

            if user is not None:
                # Set session variable to indicate user is logged in
                session['logged_in'] = True
                session['user_id'] = user[0]
                return redirect(url_for('list_accounts'))
    
    return render_template('login.html')

# Register route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Add any other registration fields as needed

        db = connect_to_database()
        if db is not None:
            cursor = db.cursor()
            query = 'INSERT INTO users (username, password) VALUES (%s, %s)'
            values = (username, password)
            cursor.execute(query, values)
            db.commit()
            db.close()

            return redirect(url_for('login'))
    
    return render_template('register.html')

# Protected routes - require login

# Open a new account
@app.route('/open_account', methods=['GET', 'POST'])
def open_account():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    if request.method == 'POST':
        account_number = request.form['account_number']
        account_holder = request.form['account_holder']
        phone_number = request.form['phone_number']
        address = request.form['address']
        email = request.form['email']

        db = connect_to_database()
        if db is not None:
            cursor = db.cursor()
            query = 'INSERT INTO accounts (account_number, account_holder, phone_number, address, email, balance) VALUES (%s, %s, %s, %s, %s, 0)'
            values = (account_number, account_holder, phone_number, address, email)
            cursor.execute(query, values)
            db.commit()
            db.close()

            return redirect(url_for('list_accounts'))

    return render_template('open_account.html')

# Deposit amount
@app.route('/deposit_amount', methods=['GET', 'POST'])
def deposit_amount():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    if request.method == 'POST':
        account_number = request.form['account_number']
        amount = float(request.form['amount'])

        db = connect_to_database()
        if db is not None:
            cursor = db.cursor()
            query = 'UPDATE accounts SET balance = balance + %s WHERE account_number = %s'
            values = (amount, account_number)
            cursor.execute(query, values)
            db.commit()
            db.close()

            return redirect(url_for('list_accounts'))

    return render_template('deposit_amount.html')

# Withdraw amount
@app.route('/withdraw_amount', methods=['GET', 'POST'])
def withdraw_amount():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    if request.method == 'POST':
        account_number = request.form['account_number']
        amount = float(request.form['amount'])

        db = connect_to_database()
        if db is not None:
            cursor = db.cursor()
            query = 'UPDATE accounts SET balance = balance - %s WHERE account_number = %s'
            values = (amount, account_number)
            cursor.execute(query, values)
            db.commit()
            db.close()

            return redirect(url_for('list_accounts'))

    return render_template('withdraw_amount.html')

#balance_enquiry
@app.route('/balance_enquiry', methods=['GET', 'POST'])
def balance_enquiry():
    if request.method == 'POST':
        account_number = request.form['account_number']

        db = connect_to_database()
        if db is not None:
            cursor = db.cursor()
            query = 'SELECT balance FROM accounts WHERE account_number = %s'
            values = (account_number,)
            cursor.execute(query, values)
            result = cursor.fetchone()
            db.close()

            if result is not None:
                balance = result[0]
                return render_template('balance_enquiry.html', account_number=account_number, balance=balance)

    return render_template('balance_enquiry.html', account_number=None, balance=None)







# List accounts
@app.route('/list_accounts')
def list_accounts():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    db = connect_to_database()
    if db is not None:
        cursor = db.cursor()
        query = 'SELECT * FROM accounts'
        cursor.execute(query)
        result = cursor.fetchall()
        db.close()

        return render_template('list_accounts.html', accounts=result)

# Edit account details
@app.route('/edit_account/<int:account_id>', methods=['GET', 'POST'])
def edit_account(account_id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    db = connect_to_database()
    if db is not None:
        cursor = db.cursor()
        query = 'SELECT * FROM accounts WHERE id = %s'
        values = (account_id,)
        cursor.execute(query, values)
        account = cursor.fetchone()

        if account is not None:
            if request.method == 'POST':
                account_holder = request.form['account_holder']
                phone_number = request.form['phone_number']
                address = request.form['address']
                email = request.form['email']

                update_query = 'UPDATE accounts SET account_holder = %s, phone_number = %s, address = %s, email = %s WHERE id = %s'
                update_values = (account_holder, phone_number, address, email, account_id)
                cursor.execute(update_query, update_values)
                db.commit()
                db.close()

                return redirect(url_for('list_accounts'))

            return render_template('edit_account.html', account=account)

    return redirect(url_for('list_accounts'))

# Close account
@app.route('/close_account/<int:account_id>')
def close_account(account_id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    db = connect_to_database()
    if db is not None:
        cursor = db.cursor()
        query = 'DELETE FROM accounts WHERE id = %s'
        values = (account_id,)
        cursor.execute(query, values)
        db.commit()
        db.close()

    return redirect(url_for('list_accounts'))

# Logout route
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

# Main route
@app.route('/')
def main():
    return redirect(url_for('list_accounts'))

if __name__ == '__main__':
    app.run(debug=True)
