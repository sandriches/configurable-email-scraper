import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests
from dotenv import load_dotenv
import os

load_dotenv()

# Set the URL of the website to check
url = 'https://www.example.com'

# Set the number of times to check per day
times_per_day = 4

# Set the SMTP server and login details (this example uses Gmail)
smtp_server = os.getenv('SMTP_SERVER')
smtp_port = int(os.getenv('SMTP_PORT'))
smtp_password = os.getenv('SMTP_PASSWORD')

# Set the sender and recipient email addresses
sender_email = os.getenv('SENDER_EMAIL')
recipient_email = os.getenv('RECIPIENT_EMAIL')
smtp_user = sender_email

def send_email():
    # Create a multipart message and set headers
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject'] = 'Apartment is available!!!! Gogogo'

    # Add body to email
    body = 'A house is available on {}'.format(url)
    message.attach(MIMEText(body, 'plain'))

    # Create secure connection with server and send email
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_user, smtp_password)
    text = message.as_string()
    server.sendmail(sender_email, recipient_email, text)
    server.quit()

def check_availability():
    # Get the HTML of the website
    response = requests.get(url)
    html = response.text
    if ('Apartment is available' in html):
        send_email()

# Calculate the time interval between checks in seconds
interval = 24 * 60 * 60 / times_per_day

    # Continuously check for availability at the specified interval
while True:
    time.sleep(interval)
    check_availability()