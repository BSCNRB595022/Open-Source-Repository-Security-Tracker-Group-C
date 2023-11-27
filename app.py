import asyncio
import logging
import os

import grequests
import requests
from flask import (
    Flask,
    abort,
    flash,
    jsonify,
    redirect,
    render_template,
    request,
    send_from_directory,
    url_for,
)

from flask import Flask, render_template, request, redirect, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
app.config["SECRET_KEY"] = "your_secret_key_here"
app.config["UPLOAD_FOLDER"] = os.path.join(os.getcwd(), "uploads")

db = SQLAlchemy(app)

if not os.path.exists(app.config["UPLOAD_FOLDER"]):
    os.makedirs(app.config["UPLOAD_FOLDER"])

log_file_path = os.path.join(os.getcwd(), "app.log")
handler = logging.FileHandler(log_file_path)
handler.setLevel(logging.ERROR)
app.logger.addHandler(handler)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    subject = db.Column(db.String(120))
    message = db.Column(db.Text)


class Issue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=False)
    source = db.Column(db.String(120))

# Create the database tables
# db.create_all()

# Define routes
@app.route("/")
def index():
    return render_template("index.html")


@app.route('/register', methods=['POST'])
def register():
    try:
        # Get form data
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirmPassword']

        # Simple validation
        if not username or not email or not password or not confirm_password:
            return jsonify({'error': 'All fields are required'}), 400

        if password != confirm_password:
            return jsonify({'error': 'Passwords do not match'}), 400

        # Check if the username or email is already in use
        if User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first():
            return jsonify({'error': 'Username or email already in use'}), 400

        # Create a new user
        new_user = User(username=username, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message': 'Registration successful'}), 200
    
    except Exception as e:
        print(f"Error during registration: {e}")
        return jsonify({'error': 'Registration failed'}), 500
    



    
@app.route('/login')
def login():
    return render_template('login.html')




# Add this error handler to return JSON for errors
@app.errorhandler(401)
def unauthorized(e):
    return jsonify(error=str(e)), 401


@app.route("/contact", methods=["POST"])
def contact():
    try:
        data = request.form
        full_name = data["full-name"]
        email = data["email"]
        subject = data.get("subject", "")
        message = data.get("message", "")

        new_contact = Contact(
            full_name=full_name, email=email, subject=subject, message=message
        )
        db.session.add(new_contact)
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print(f"Error committing to the database: {str(e)}")
            app.logger.error(f"Error committing to the database: {str(e)}")
            return jsonify({"message": "Error committing to the database"}), 500

        # Redirect to the home page after storing contact information
        return redirect(url_for("index"))

    except Exception as e:
        # Log the error for debugging purposes
        app.logger.error(f"Error during contact form submission: {str(e)}")
        return jsonify({"message": "Internal server error"}), 500


@app.route("/dashboard")
def dashboard():
    issues = Issue.query.all()
    return render_template("dashboard.html", issues=issues)


VIRUSTOTAL_API_KEY = "dab8eaf854234d639b83f4f01cc6eef28b30445737da3a2b94b121bc8468592a"


def scan_url_async(target_url):
    api_url = "https://www.virustotal.com/vtapi/v2/url/scan"
    params = {"apikey": VIRUSTOTAL_API_KEY, "url": target_url}

    try:
        response = requests.post(api_url, params=params)
        response.raise_for_status()  # Raise an error for bad responses
        result = response.json()
        return result
    except requests.exceptions.RequestException as e:
        app.logger.error(f"Error scanning URL: {str(e)}")
        return {"message": "Error scanning URL"}


@app.route("/scan-url", methods=["POST"])
def scan_url():
    try:
        data = request.get_json()
        url = data.get("url")

        if not url:
            return jsonify({"message": "Invalid URL"}), 400

        result = scan_url_async(url)

        if result.get("response_code") == 1:
            return jsonify({"message": "URL is clean"})
        else:
            return jsonify({"message": "Source URL is suspicious"})

    except Exception as e:
        app.logger.error(f"Error scanning URL: {str(e)}")
        return jsonify({"message": "Internal server error"}), 500


@app.route("/dashboard", methods=["POST"])
def submit_issue():
    try:
        title = request.form.get("title")
        description = request.form.get("description")
        source = request.form.get("source")

        # Validate the form data
        if not title or not description or not source:
            return jsonify({"message": "Please fill in all required fields"}), 400

        # Scan the source URL using VirusTotal API
        result = scan_url_async(source)

        # Check if the scan was successful
        if result.get("response_code") == 1:
            # URL is clean
            flash("File uploaded successfully.")
            scan_result = "URL is clean"
        else:
            # URL is suspicious, handle accordingly
            flash("Source URL is suspicious.")
            scan_result = "Source URL is suspicious"

        # Check if a file has been uploaded
        file = request.files.get("file")
        if file:
            # Save the file to the uploads directory
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
            flash("File uploaded successfully.")
        else:
            flash("No file uploaded.")

        # Create a new issue
        new_issue = Issue(title=title, description=description, source=source)

        # Add the new issue to the database
        db.session.add(new_issue)
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print(f"Error committing to the database: {str(e)}")
            app.logger.error(f"Error committing to the database: {str(e)}")
            return jsonify({"message": "Error committing to the database"}), 500

        # Modify the response to include VirusTotal results
        return render_template(
            "dashboard.html", issues=Issue.query.all(), virustotal_result=result
        )

    except Exception as e:
        # Log the error for debugging purposes
        app.logger.error(f"Error submitting issue: {str(e)}")
        return jsonify({"message": "Internal server error"}), 500


if __name__ == "__main__":
    with app.app_context():
        try:
            # Create the database tables
            db.create_all()
            app.logger.info("Database tables created successfully")
        except Exception as e:
            # Log the error and print it for debugging purposes
            app.logger.error(f"Error creating database tables: {str(e)}")
            print(f"Error creating database tables: {str(e)}")

    # Run the app using gunicorn with the gevent worker
    app.run(threaded=False, host="127.0.0.1", port=5000)
