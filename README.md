# Open-Source Repository Security Tracker

## Project Description

This project is a software engineering assignment for the course BSC3106: Software Engineering 2 at St. Paul's University. The aim of this project is to develop a tool that can track the security issues of open-source repositories on GitHub.

## Lecturer

This project is supervised by Madam Cecilia Angela Nanfuka, a lecturer at St. Paul's University.

## Participants

The participants of this project are:

- BSCNRB548222
- BSCNRB587922
- BSCNRB443722
- BSCNRB591520
- BSCNRB595022

## Installation

This documentation provides step-by-step instructions for installing and running the project. The project is a Flask-based web application for managing user accounts and reporting issues. It uses SQLite as its database.

## Prerequisites

Before you begin, ensure you have the following prerequisites:

- Python 3.7 or higher installed
- Pip (Python package manager)
- A terminal or command prompt
- A web browser

## Installation

1. **Clone the Repository**: Start by cloning the project repository to your local machine. You can do this by running the following command:

    ```bash
    git clone https://github.com/BSCNRB595022/Open-Source-Repository-Security-Tracker-Group-C.git
    ```

2. **Navigate to Project Directory**: Change your current working directory to the project folder:

    ```bash
    cd Open-Source-Repository-Security-Tracker-Group-C
    ```

3. **Create a Virtual Environment (Optional but Recommended)**: It's a good practice to create a virtual environment to isolate project dependencies. You can create one using the following command:

    ```bash
    python -m venv venv
    ```

4. **Activate the Virtual Environment**: Activate the virtual environment:

    - On Windows:

    ```bash
    venv\Scripts\activate
    ```

    - On macOS and Linux:

    ```bash
    source venv/bin/activate
    ```

5. **Install Dependencies**: Install the project's Python dependencies using pip:

    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

Now that you've installed the project, you can run the application.

1. **Initialize the Database**: Before running the application, you need to create the database tables. Run the following command to do this:

    ```bash
    python database.py
    ```

2. **Start the Application**: To start the Flask application, run the following command:

    ```bash
    python app.py
    ```

3. **Access the Application**: Open your web browser and go to `http://localhost:5000`. You should see the application's home page.

## Usage

The project consists of several routes that you can access via the web interface:

- `/`: Home page with options to login or register.
- `/login`: Login page for existing users.
- `/register`: Registration page for new users.
- `/dashboard`: Dashboard displaying a list of reported issues.
- `/report_issue`: Route for reporting new issues.

## Clearing the Database

If you need to clear the database for testing or other purposes, you can use the 2 scripts provided:

```bash
reset_issue_table_db.py
```
```bash
reset_issue_table_db.py
```

## Project Structure

The project contains two main directories:

- **static**: This directory contains static files such as CSS and JavaScript used for styling and functionality in the web application.

- **templates**: This directory contains HTML templates for different pages of the application.

## Conclusion

You've successfully installed and run the project. You can now register, log in, report issues, and view the dashboard. Feel free to explore and use the web application as needed. If you encounter any issues, create an issue in the issue tab.
