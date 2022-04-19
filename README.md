# Email Sender in Python3
This is a project made by Zhaklin Braka. A simple python3 email sender based on user's configuration file.

## Install
Clone the repo:  
```bash
git clone https://github.com/zhaklinn/Email-Sender-py3.git
```

## Requirements
Make sure you have the following libraries installed:
```
- smtplib
- ssl
- email
- email.mime.text
- email.mime.multipart
- email.mime.base
- sys
- configparser
- argparse
```

You can install the libraries automatically by executing:
```bash
pip3 install -r requirements.txt
```

## Configuration
Make sure to change the values on **config.ini** to your needs. If you don't want to set a value, simply put **None**.

## Usage
To run the program, you simply need to execute:
```bash
python3 email_sender.py
```

To run the program with the configuration files:
```python
python3 email_sender.py -d
```

To add an attachment to the email (Linux):
```python3
python3 email_sender.py -f "/path/to/file" 
```

To add an attachment to the email (Windows):
```python3
python3 email_sender.py -f "C:\Users\username\path\to\file" 
```

Optionally you can use both **-d** and **-f** 

## Demo

Demo 1
```
python3 email_sender.py -d

~~~ Authenticaion Portal ~~~
Enter your email: your email
Enter your password: your password
Successfuly authenticated!

~~~ Welcome to Email Sender by Zhaklina Braka ~~~
Email subject: This is a demo
Do you want to attach your message or type it directly in terminal? (a/t): t
Enter the email body in HTML or plaintext form (press CTRL+D when you are done):
This is a body example

~~~ Email preview: ~~~

From: demo@gmail.com
To: testing@gmail.com, client1@gmail.com, client2@gmail.com
Cc: testing2@gmail.com
Bcc: testing3@gmail.com
Subject: This is a demo email
File Attachment: No file attached
Body: This is a body example

----------------------
Best regards, Email send by Your Name

Are you sure you want to send this email? [y/n]: y
Email saved to logs!
Email sent!
```

Demo 2
```
python3 email_sender.py
~~~ Authenticaion Portal ~~~
Enter your email: your email
Enter your password: your password
Successfuly authenticated!

~~~ Welcome to Email Sender by Zhaklina Braka ~~~
Receiver email: demo@gmail.com
Signature: This is a demo signature
CC: None
BCC: None
Email subject: This is a test email subject
Do you want to attach your message or type it directly in terminal? (a/t): t
Enter the email body in HTML or plaintext form (press CTRL+D when you are done):
<html>    
    <h1>Hello this is a header</h1>
</html>

~~~ Email preview: ~~~

From: client1@gmail.com
To: client2@gmail.com
Cc: None
Bcc: None
Subject: This is a test email subject
File Attachment: No file attached
Body: <html>
    <h1>Hello this is a header</h1>
</html>

----------------------
This is a demo signature

Are you sure you want to send this email? [y/n]: y
Email saved to logs!
Email sent!

```

## Known bugs
During the test engagement, there was no bug detected. Feel free to open an issue if you come across any bug(s).
