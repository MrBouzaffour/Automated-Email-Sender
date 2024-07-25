# Automated Email Sender

This Python script allows users to send automated emails with ease. Leveraging `smtplib` and `email` libraries, the script supports plain text and HTML emails. It's designed to be secure and flexible, using environment variables to handle email credentials.

## Features
- Simple and straightforward email sending
- Support for plain text and HTML emails
- Attach files to emails
- Schedule emails to be sent at a specific time
- Secure credential management with environment variables
- Customizable email content
- Error handling and logging
- Send emails to multiple recipients
- Configurable SMTP server settings
- Secure email content with encryption

## Setup

### 1. Clone the Repository:
```sh
git clone https://github.com/yourusername/automated-email-sender.git
cd automated-email-sender
```

### 2. Install Dependencies:
```sh
pip install python-dotenv
```

### 3. Configure Environment Variables:
Create a .env file in the root directory and add your email credentials:
```sh
EMAIL_ADDRESS=your_email@example.com
EMAIL_PASSWORD=your_password
```

### 4. Run the Script:
```sh
python main.py
```
