from flask import Flask, render_template, redirect, url_for, request, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Home page route
@app.route('/')
def home():
    return render_template('home.html')

# Dashboard route
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# ATM test route
@app.route('/test-atm')
def test_atm():
    return render_template('test_atm.html')

# Bank login route
@app.route('/bank-login', methods=['GET', 'POST'])
def bank_login():
    if request.method == 'POST':
        # Logic to handle bank login, e.g. checking credentials
        username = request.form['username']
        password = request.form['password']
        if username == "user" and password == "pass":
            flash('Login Successful', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid Credentials', 'danger')
    return render_template('bank_login.html')

# Register route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Logic to register new users
        username = request.form['username']
        password = request.form['password']
        flash('Registration Successful', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Logic to handle login
        username = request.form['username']
        password = request.form['password']
        if username == "user" and password == "pass":
            flash('Login Successful', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid Credentials', 'danger')
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
