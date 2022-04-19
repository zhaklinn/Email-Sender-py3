#project by Zhaklina Braka
#please read the readme.md for more information

import smtplib, ssl
#importing the following libraries to support HTML markup
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders #library to encode the file content in base64
import sys #library imported to read the user input with newlines
import configparser #library to read the config.ini file
import argparse #library to parse the arguments when executing the python script

#to make this work, make sure 2FA is disabled and "Less secure app access" is turned on.
#it can be turned on under "Manage my Google account" -> Security

#some default configurations
port = 465  # For SSL which is a more secure connection
smtp_server = "smtp.gmail.com"

#first thing, we need to authenticate, so lets read the encrypted md5 password from config
config = configparser.ConfigParser() #initialize the config parser library
config.read("config.ini") #read the config file
# Add the structure to the config file located in this folder

#ask the user to enter the password
count = 0 #the tries of the user
print("~~~ Authenticaion Portal ~~~")
while count < 3:
    user_email = input("Enter your email: ")
    user_password = input("Enter your password: ")
    
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server: #here happens the authentication
        try:
            server.login(user_email, user_password)
            print("Successfuly authenticated!\n")
            break
        except:
            count += 1
            print("Incorrect email or password! You have {} left chances".format(3 - count))

if count >= 3:
    exit()    
#authentication process ends here    

#print a lovely welcome sign
print("~~~ Welcome to Email Sender by Zhaklina Braka ~~~")

#first we define user's input with argument parsing
parser = argparse.ArgumentParser(description='A simple but functional email sender')
parser.add_argument('-d', help='Load the default configuration file', dest='config_parse', action='store_true')
parser.add_argument('-f', help='Insert an attachment', dest='add_attachment', action='store')
arg = parser.parse_args()

if arg.config_parse:
    config = configparser.ConfigParser() #initialize the config parser library
    config.read("config.ini") #read the config file
    # Add the structure to the config file located in this folder
    userinfo = config["user_info"]
    receiver_email = userinfo["recipient"]
    signature = userinfo["signature"]
    cc = userinfo["cc"]
    bcc = userinfo["bcc"]

if not arg.config_parse:
    receiver_email = input("Receiver email: ")
    signature = input("Signature: ")
    cc = input("CC: ")
    bcc = input("BCC: ")

subject_email = input("Email subject: ")
body_choice = input("Do you want to attach your message or type it directly in terminal? (a/t): ")

if body_choice == "t":
    print("Enter the email body in HTML or plaintext form (press CTRL+D when you are done):")
    body_email = sys.stdin.read()
elif body_choice == "a":
    file_path = input("Enter the local path to the file: ")
    f = open(file_path, "r") #r = we only give permission to read the file
    body_email = f.read()
    f.close() #closes the file when we are done

#add the signature to the email body    
body_email = body_email + "\n----------------------\n" + signature

#constructing the email subject
message = MIMEMultipart("alternative") #must be "alternative" to support html
message["Subject"] = subject_email
message["From"] = user_email
message["To"] = receiver_email
message["Cc"] = cc
message["Bcc"] = bcc

# Turn the email into plaintext or html based on user's input
if "<html>" in body_email:
    part = MIMEText(body_email, "html")
else:
    part = MIMEText(body_email, "plain")
    
#attach the whole html content
message.attach(part)

#add the file attachment if the user specified the -f argument
if arg.add_attachment:
    filename = arg.add_attachment
    
    with open(filename, 'rb') as file:
        part = MIMEBase('application', "octet-stream")
        part.set_payload(file.read())
        
    encoders.encode_base64(part) #encode the file content in base64 to avoid any error when readind (because of non-readable asci characters)
    part.add_header('Content-Disposition', 'attachment; filename={}'.format(filename))
    message.attach(part) #attach the file in email

elif not arg.add_attachment:
    filename = "No file attached"

#print the email to the user before sending it
print("\n~~~ Email preview: ~~~\n")
print("From: {}".format(user_email))
print("To: {}".format(receiver_email))
print("Cc: {}".format(cc))
print("Bcc: {}".format(bcc))
print("Subject: {}".format(subject_email))
print("File Attachment: {}".format(filename))
print("Body: {}".format(body_email))
confirm_send = input("\nAre you sure you want to send this email? [y/n]: ")

if confirm_send == "y" or confirm_send == "Y":
    #first we save the email in the log file
    logs_file = open("sent_email.logs","a") #a for append, it means that we add information without deleting the content of the log first
    logs_file.write("From: {}\n".format(user_email))
    logs_file.write("To: {}\n".format(receiver_email))
    logs_file.write("Cc: {}\n".format(cc))
    logs_file.write("Bcc: {}\n".format(bcc))
    logs_file.write("Subject: {}\n".format(subject_email))
    logs_file.write("File Attachment: {}\n".format(filename))
    logs_file.write("Body: {}\n".format(body_email))
    logs_file.write("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n")
    logs_file.close()
    print("Email saved to logs!")
    
    #this code is for authentication + email sending
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(user_email, user_password)
        server.sendmail(user_email, receiver_email.split(','), message.as_string())
        print("Email sent!")

elif confirm_send == "n" or confirm_send == "N":
    exit()
