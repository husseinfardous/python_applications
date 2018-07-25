# Backend

# Sends Population Statistics on Age to Users

# Import Modules
from email.mime.text import MIMEText
import smtplib



def send_email(email, age, age_count, average_age):

    # Login Credentials to Gmail Account that Sends the Information
    from_email = "dummy.email476@gmail.com"
    from_password = "funny_dummy"

    # User Email Address
    to_email = email

    # Email Subject and Message
    subject = "Age Data"
    message = "You are <strong> %s </strong> years old. <br> In a population of <strong> %s </strong> people, the average age is <strong> %s </strong> years old. <br> Thank you for your time!" % (age, age_count, average_age)

    # Change Email Message Format from Plain Text to HTML Text
    msg = MIMEText(message, "html")
    msg["From"] = from_email
    msg["To"] = to_email
    msg["Subject"] = subject

    # Connect to Gmail, Login, and Send the Message
    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)
