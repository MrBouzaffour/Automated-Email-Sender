import os
import smtplib
from email.mime.multipart import  MIMEMultipart
from email.mime.text import  MIMEText
from email.mime.application import  MIMEApplication
import logging
from datetime import datetime, timedelta
import time

EMAIL_ADDRESS = "abouzefour323@gmail.com"
PASSWORD = "a34432604"

# Set up logging
logging.basicConfig(filename='email_sender.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

def send_email(to_emails, subject, body, html_body=None, attachments=None, send_at=None):
    # Create the email header
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = ", ".join(to_emails)
    msg['Subject'] = subject

    # Attach the email body
    msg.attach(MIMEText(body, 'plain'))
    if html_body:
        msg.attach(MIMEText(html_body, 'html'))

    # Attach any files
    if attachments:
        for attachment in attachments:
            with open(attachment, 'rb') as f:
                part = MIMEApplication(f.read(), Name=os.path.basename(attachment))
                part['Content-Disposition'] = f'attachment; filename="{os.path.basename(attachment)}"'
                msg.attach(part)

    # Schedule email if send_at is provided
    if send_at:
        delay = (send_at - datetime.now()).total_seconds()
        if delay > 0:
            time.sleep(delay)

    # Connect to the server and send the email
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        text = msg.as_string()
        server.sendmail(EMAIL_ADDRESS, to_emails, text)
        server.quit()
        logging.info(f"Email sent successfully to {to_emails}")
    except Exception as e:
        logging.error(f"Failed to send email: {e}")

# Example usage
if __name__ == "__main__":
    to_emails = ["ahmedbouzaffour2002@gmail.com"]
    subject = "Test Email"
    body = "This is a test email sent from an automated Python script."
    html_body = "<h1>This is a test email</h1><p>sent from an automated Python script.</p>"
    attachments = []
    send_at = datetime.now() + timedelta(minutes=1)  # Send email after 1 minute
    send_email(to_emails, subject, body, html_body, attachments, send_at)
