# 🐞 Bug Tracker Web Application

This is a simple internal **Bug Tracker Web Application** built using **Python (Flask), HTML, CSS, and JavaScript**. It allows users to sign up, log in, report bugs, and view submitted bugs on a dashboard — all stored using local CSV files instead of a traditional database.

---

## 📁 Create the Project in this Structure

bug_tracker/
├── static/
│   ├── css/
│   │   └── style.css   # Stylesheet for all pages
│   └── js/
│       └── script.js   # JavaScript file (currently minimal)
├── templates/
│   ├── index.html      # Home page
│   ├── login.html      # Login page
│   ├── signup.html     # Signup page
│   ├── dashboard.html  # User dashboard after login
│   └── bug_form.html   # Bug report form
├── app.py              # Main Python (Flask) application
├── README.md           # Project description file


---

## After pasting the codes open new terminal and Install flask with the below command:

pip install flask


## Run the application by using the below command:

python app.py

@jagan5 ➜ /workspaces/Bug-Tracker-Web-Application (main) $ python app.py
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 102-454-177

Copy this Link "http://127.0.0.1:5000" and paste it in a browser.

## ✅ Features

- User Signup and Login
- Bug Submission Form
- Dashboard for Viewing All Bugs
- Priority Selection (Low, Medium, High)
- Session-based Authentication
- CSV File Storage (no database)
- Clean, responsive UI with HTML, CSS, and JavaScript

---

## 🧠 Skills & Experience Gained

- Hands-on experience in developing and maintaining an internal web application
- Gained working knowledge of Python, HTML, CSS, and JavaScript
- Learned how to handle user authentication and data management
- Explored file-based storage and logic for program debugging
- Discovered and monitored software bugs and discrepancies

---

## 🛠️ Technologies Used

| Component     | Technology          |
|---------------|---------------------|
| Backend       | Python (Flask)      |
| Frontend      | HTML, CSS, JavaScript |
| Storage       | CSV files (`users.csv`, `bugs.csv`) |
| Templates     | Jinja2 (Flask Templates) |

---


