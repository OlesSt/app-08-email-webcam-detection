import os
import smtplib
import imghdr
from email.message import EmailMessage
email = "oles1stepanov@gmail.com"
password = os.getenv("PASSWORD")


def send_email(image_path):
    email_message = EmailMessage()
    email_message["Subject"] = "New object showed"
    email_message.set_content("Hey. Detected a new object")

    with open(image_path, "rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))
    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(email, password)
    gmail.sendmail(email, email, email_message.as_string())
    gmail.quit()