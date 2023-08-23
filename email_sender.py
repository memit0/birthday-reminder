import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from app2 import password
from birthday_checker import name_of_birthday_people as names

# Email configuration
smtp_server = 'smtp.gmail.com' #server used 
smtp_port = 587  # Use 465 for SSL/TLS
sender_email = 'battalzach@gmail.com'
sender_password = password
receiver_email = 'jaheso6277@vikinoko.com'
subject = 'Birthday Email'
message_text = "It's  " + names + " birthday today make sure to wish them a happy birthday!"

# Create the email message
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = subject
message.attach(MIMEText(message_text, 'plain'))

# Connect to the SMTP server and send the email
try:
    smtp_connection = smtplib.SMTP(smtp_server, smtp_port)
    smtp_connection.starttls()  
    smtp_connection.login(sender_email, sender_password)
    smtp_connection.sendmail(sender_email, receiver_email, message.as_string())
    print("Email sent successfully.")
except Exception as e:
    print("Error sending email:", e)
finally:
    smtp_connection.quit()
