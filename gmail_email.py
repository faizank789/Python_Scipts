import smtplib

sender_email = "sender@gmail.com"
receiver_email = "receiver@gmail.com"
password = "sender_email_password"

message = """\
Subject: Your Subject

This is the body of your email."""

with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
