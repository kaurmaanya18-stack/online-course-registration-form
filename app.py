
from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("c_registration.html")


@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    email = request.form.get("email_id")
    mobile = request.form.get("mobile")
    age = request.form.get("age")
    gender = request.form.get("gender")
    skills = request.form.getlist("skills")
    other_skills = request.form.get("other_skills")
    course = request.form.get("course")
    form_name = request.form.get("form_name")
    registration_date = request.form.get("dt")
    registration_time = request.form.get("tm")
    reason = request.form.get("y")

    skills_text = ", ".join(skills)

    connection = sqlite3.connect("registrations.db")
    cursor = connection.cursor()

    try:
        cursor.execute("""
            INSERT INTO registrations (
                name, email, course, mobile, age, gender,
                skills, other_skills, form_name,
                registration_date, registration_time, reason
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            name, email, course, mobile, age or None, gender,
            skills_text, other_skills, form_name,
            registration_date, registration_time, reason
        ))

        connection.commit()

    finally:
        connection.close()

    return f"""
    <h2>Registration Successful</h2>
    <p>Name: {name}</p>
    <p>Email: {email}</p>
    <p>Mobile: {mobile}</p>
    <p>Age: {age}</p>
    <p>Gender: {gender}</p>
    <p>Course: {course}</p>
    <p>Skills: {skills_text}</p>
    <p>Other skills: {other_skills or 'Not provided'}</p>
    <p>Reason: {reason or 'Not provided'}</p>
    """


if __name__ == "__main__":
    app.run(debug=True)
