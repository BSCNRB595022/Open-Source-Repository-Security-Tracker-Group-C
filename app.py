# this is the main python file for the flask app, it contains all the logics, routes and the database connections.

import sqlite3

from flask import Flask, jsonify, redirect, render_template, request, url_for

from database import create_issue_table, create_table

app = Flask(__name__)


# Create the database table if it doesn't exist
def create_table():
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)"
    )
    connection.commit()
    connection.close()


create_table()
create_issue_table()


@app.route("/", methods=["GET", "POST"])
def home():
    # html to be displayed login or register and redirect to the respective page
    return render_template("home.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    message = None  # Initialize message variable
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        connection = sqlite3.connect("users.db")
        cursor = connection.cursor()
        cursor.execute(
            "SELECT * FROM users WHERE username=? AND password=?", (username, password)
        )
        user = cursor.fetchone()
        connection.close()
        if user:
            # Redirect to the dashboard page on successful login
            return redirect(url_for("dashboard", username=username))
        else:
            message = "Incorrect credentials. Please check your username and password."

    return render_template(
        "login.html", message=message
    )  # Pass the message to the template


@app.route("/register", methods=["GET", "POST"])
def register():
    message = None  # Initialize message variable
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        connection = sqlite3.connect("users.db")
        cursor = connection.cursor()

        # Check if the username already exists in the database
        cursor.execute("SELECT id FROM users WHERE username=?", (username,))
        existing_user = cursor.fetchone()

        if existing_user:
            connection.close()
            message = "Registration failed. This username is already in use."
        else:
            cursor.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)",
                (username, password),
            )
            connection.commit()
            connection.close()

            return redirect(url_for("login"))

    return render_template(
        "register.html", message=message
    )  # Pass the message to the template


@app.route("/dashboard")
def dashboard():
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM issues")
    issues = cursor.fetchall()
    connection.close()
    return render_template("dashboard.html", issues=issues)


@app.route("/report_issue", methods=["POST"])
def report_issue():
    if request.method == "POST":
        title = request.form["title"]
        description = request.form["issue-description"]
        severity = request.form["issue-severity"]
        source = request.form["issue-source"]

        connection = sqlite3.connect("users.db")
        cursor = connection.cursor()

        cursor.execute(
            "INSERT INTO issues (title, description, severity, source) VALUES (?, ?, ?, ?)",
            (title, description, severity, source),
        )
        connection.commit()
        connection.close()

        # Debug: Check if the issue was added to the database
        print("Issue added to the database")

        # Fetch the updated list of issues
        connection = sqlite3.connect("users.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM issues")
        issues = cursor.fetchall()
        connection.close()

        # Debug: Check if the list of issues is retrieved correctly
        print("List of issues retrieved:", issues)

        # Redirect back to the dashboard with the updated issues
        return render_template("dashboard.html", issues=issues)

    return redirect(url_for("dashboard"))


@app.route("/get_filtered_issues", methods=["POST"])
def get_filtered_issues():
    if request.method == "POST":
        severity = request.json.get("severity")
        sort_by = request.json.get("sort")
        search = request.json.get("search")

        print("Severity:", severity)
        print("Sort By:", sort_by)
        print("Search:", search)

        connection = sqlite3.connect("users.db")
        cursor = connection.cursor()
        query = "SELECT * FROM issues"

        if severity != "all":
            query += f" WHERE severity = '{severity}'"

        if search:
            query += f" AND (title LIKE '%{search}%' OR description LIKE '%{search}%' OR source LIKE '%{search}%')"

        if sort_by == "severity":
            query += " ORDER BY severity"
        elif sort_by == "date":
            query += " ORDER BY id DESC"

        print("Query:", query)

        cursor.execute(query)
        issues = cursor.fetchall()
        connection.close()

        print("Filtered Issues:", issues)

        # Return filtered issues as JSON data
        return jsonify(issues=issues)

    return jsonify(issues=[])


if __name__ == "__main__":
    app.run(debug=True)


if __name__ == "__main__":
    app.run(debug=True)
