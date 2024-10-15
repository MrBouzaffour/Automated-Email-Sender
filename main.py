import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from loguru import logger
from datetime import datetime, timedelta
import time
import schedule
from validate_email import validate_email

# Load email credentials from an encrypted file
import json
with open('email_credentials.json', 'r') as f:
    email_credentials = json.load(f)

EMAIL_ADDRESS: str = email_credentials['email']
EMAIL_PASSWORD: str = email_credentials['password']

# Set up logging using Loguru
logger.add("email_sender.log", rotation="500 MB")

def send_email(to_emails: list, subject: str, body: str, html_body: str = None, attachments: list = None, send_at: datetime = None) -> None:
    logger.info("Preparing to send email.")
    
    # Validate email addresses before proceeding
    for email in to_emails:
        if not validate_email(email):
            logger.error(f"Invalid email address: {email}")
            return

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
            try:
                with open(attachment, 'rb') as f:
                    part = MIMEApplication(f.read(), Name=os.path.basename(attachment))
                    part['Content-Disposition'] = f'attachment; filename="{os.path.basename(attachment)}"'
                    msg.attach(part)
                logger.info(f"Attached file {attachment}.")
            except Exception as e:
                logger.error(f"Failed to attach file {attachment}: {e}")

    # Schedule email if send_at is provided
    if send_at:
        delay = (send_at - datetime.now()).total_seconds()
        if delay > 0:
            logger.info(f"Scheduling email to be sent after {delay} seconds.")
            schedule.every(delay).seconds.do(send_email, to_emails, subject, body, html_body, attachments)
            return

    # Connect to the server and send the email
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        text = msg.as_string()
        server.sendmail(EMAIL_ADDRESS, to_emails, text)
        server.quit()
        logger.info(f"Email sent successfully to {to_emails}")
    except Exception as e:
        logger.error(f"Failed to send email: {e}")

if __name__ == "__main__":
    logger.info("Script started.")
    
    to_emails = ["recipient1@example.com", "recipient2@example.com"]
    subject = "Test Email"
    body = "This is a test email sent from an automated Python script."
    html_body = "<h1>This is a test email</h1><p>sent from an automated Python script.</p>"
    attachments = ["test_attachment.pdf"]
    send_at = datetime.now() + timedelta(minutes=1)  # Send email after 1 minute
    
    send_email(to_emails, subject, body, html_body, attachments, send_at)
    
    while True:
        schedule.run_pending()
        time.sleep(1)

    logger.info("Script finished.")
