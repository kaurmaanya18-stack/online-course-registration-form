# Online Course Registration Form

A web-based course registration application built with Python, Flask, SQLite, HTML, and CSS. It allows users to submit registration details through a web form and stores the information in a local database.

## Features

- User-friendly course registration form
- Flask backend for handling form submissions
- SQLite database for storing registration records
- Script to view saved registrations
- Utility script to clear registration records
- Database initialization and table management

## Technologies Used

- Python
- Flask
- SQLite
- HTML
- CSS

## Project Structure

```text
online-course-registration-form/
├── app.py
├── database.py
├── view_registrations.py
├── clear_data.py
├── templates/
│   └── c_registration.html
├── .gitignore
└── README.md
```

## Installation and Setup

**1. Clone the repository**

```bash
git clone https://github.com/kaurmaanya18-stack/online-course-registration-form.git
```

**2. Navigate to the project directory**

```bash
cd online-course-registration-form
```

**3. Install Flask**

```bash
python -m pip install flask
```

**4. Initialize the database**, if it has not already been initialized automatically.

```bash
python database.py
```

**5. Run the application**

```bash
python app.py
```

Open `http://127.0.0.1:5000` in your browser.

## Utility Scripts

View saved registrations:

```bash
python view_registrations.py
```

Clear saved registration records:

```bash
python clear_data.py
```

**Note:** Clearing records permanently deletes the stored registrations. Use this script carefully.

## Learning Objectives

- Building web applications with Flask
- Handling HTML form submissions
- Connecting Python with SQLite
- Performing basic database operations
- Organizing and managing code with Git and GitHub

## Future Improvements

- Form validation and improved error handling
- Responsive user interface
- Registration confirmation messages
- Secure administrative access
- Online deployment

## Author

**Maanya Kaur**

BCA — Artificial Intelligence and Machine Learning

[GitHub Profile](https://github.com/kaurmaanya18-stack)

---

*Developed as a practical project to learn backend development and database integration.*
