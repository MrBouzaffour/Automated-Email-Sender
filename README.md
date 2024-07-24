# Automated Email Sender

This Python script allows users to send automated emails with ease. Leveraging `smtplib` and `email` libraries, the script supports plain text emails. It's designed to be secure and flexible, using environment variables to handle email credentials.

## Features
- Simple and straightforward email sending
- Secure credential management with environment variables
- Customizable email content

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
