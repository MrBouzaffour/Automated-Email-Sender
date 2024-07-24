Automated Email Sender
This Python script allows users to send automated emails with ease. Leveraging smtplib and email libraries, the script supports plain text emails. It's designed to be secure and flexible, using environment variables to handle email credentials.

Features
Simple and straightforward email sending
Secure credential management with environment variables
Customizable email content
Setup
Clone the Repository:

sh
Copy code
git clone https://github.com/yourusername/automated-email-sender.git
cd automated-email-sender
Install Dependencies:

sh
Copy code
pip install python-dotenv
Configure Environment Variables:
Create a .env file in the root directory and add your email credentials:

env
Copy code
EMAIL_ADDRESS=your_email@example.com
EMAIL_PASSWORD=your_password
Run the Script:

sh
Copy code
python send_email.py
Usage
Edit the send_email.py script to customize the recipient, subject, and body of the email. Run the script to send an email.

