# Open-Source Repository Security Tracker

## Project Description

This project is a software engineering assignment for the course BSC3106: Software Engineering 1 at St. Paul's University. The aim of this project is to develop a tool that can track the security vulnerabilities of open-source repositories on GitHub and alert the users about the potential risks.

## Lecturer

This project is supervised by Madam Cecilia Angela Nanfuka, a lecturer at St. Paul's University.

## Participants

The participants of this project are:

- BSCNRB548222
- BSCNRB587922
- BSCNRB443722
- BSCNRB591520
- BSCNRB595022

## Features

The main features of this project are:

- A web interface that allows users to enter the URL of an open-source repository on GitHub and view its security status.
- A database that stores the information about the security vulnerabilities of different repositories, such as the type, severity, and date of discovery.
- A crawler that scans the GitHub API for new or updated repositories and updates the database accordingly.
- A notification system that sends email alerts to the users when a repository they are interested in has a new or updated security vulnerability.

## Technologies

The technologies used for this project are:

- Python as the programming language
- Flask as the web framework
- SQLite as the database
- Requests as the library for HTTP requests
- BeautifulSoup as the library for HTML parsing
- SMTP as the protocol for email sending

## Installation and Usage

To install and run this project, follow these steps:

1. Clone this repository to your local machine using `git clone https://github.com/...`
2. Navigate to the project directory using `cd ...`
3. Install the required dependencies using `pip install -r requirements.txt`
4. Run the web app using `python app.py`
5. Open your browser and go to [http://localhost:5000](http://localhost:5000) to access the web interface
6. Enter the URL of an open-source repository on GitHub and click on "Check Security" to view its security status
7. Enter your email address and click on "Subscribe" to receive email alerts about the security vulnerabilities of the repository

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
