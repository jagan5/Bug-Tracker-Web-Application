from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

users = {}
bugs = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users:
            flash('Username already exists')
            return redirect(url_for('signup'))
        users[username] = generate_password_hash(password)
        flash('Signup successful! Please log in.')
        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and check_password_hash(users[username], password):
            session['username'] = username
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid Credentials')
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html', bugs=bugs)

@app.route('/report', methods=['GET', 'POST'])
def report_bug():
    if 'username' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        bugs.append({
            'title': title,
            'description': description,
            'reporter': session['username'],
            'status': 'Open'
        })
        return redirect(url_for('dashboard'))
    return render_template('bug_form.html')

@app.route('/close/<int:bug_index>', methods=['POST'])
def close_bug(bug_index):
    if 'username' not in session:
        return redirect(url_for('login'))
    if 0 <= bug_index < len(bugs):
        bugs[bug_index]['status'] = 'Closed'
    return redirect(url_for('dashboard'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
