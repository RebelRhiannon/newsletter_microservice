# newsletter_microservice - README

---
**Overview**
This microservice allows users to:
1) Subscribe to a monthly cybersecurity newsletter
2) Check their subscription status
3) Update their email address
4) Unsubscribe from the newsletter
5) Send the newsletter to all subscribers

It is built with Python (flask) and currently uses **Mailtrap SMTP** for email testing. 
To send real emails, this must be replaced with Mailgun or another SMTP provider. 

---
**Setup Instructions**

Install required dependencies

Windows Setup:
1) Download Python from https://www.python.org/downloads/
2) During installation, check "Add Python to Path".
3) Verify installataion by running: python --version
4) Install flask and dependencies: pip install flask flask-cors requests

Mac/Linux Setup:
1) Install Python if not already installed: bew install python
2) Verify installation: python3 --version
3) Install Flask and dependencies: pip3 install flask flask-cors requests
---
**Set Up Environment Variables for email SMTP**

Use MailTrap (Testing Mode)
1) Sign up at https://mailtrap.io/
2) Go to Email Testing --> SMTP settings and copy your username and password
3) Set environment variables:

Mac/Linux 
(bash/zsh):
export MAILTRAP_USER="your-mailtrap-username"
export MAILTRAP_PASS="your-mailtrap-password"

To verify:
(You should be able to see your username if it is exported correctly) 
echo $MAILTRAP_USER 

(You should be able to see your password if it is exported correctly)
echo $MAILTRAP_PASS

Windows
(PowerShell):
$Env:MAILTRAP_USER="your-mailtrap-username"
$Env:MAILTRAP_PASS="your-mailtrap-password"

To verify:
(You should be able to see your username if it is exported correctly) 
Get-ChildItem Env:MAILTRAP_USER

(You should be able to see your password if it is exported correctly)
Get-ChildItem Env:MAILTRAP_PASS

---
**Running the Microservice**
Start the Flask server: Python app.py or (if using Python 3) python3 app.py

By Default: the server will run at http://127.0.0.1:5000/

---
**API Endpoints and Usage**
1) Subscribe to Newsletter
   Endpoint: POST/subscribe
   Request Example: 
    {
      "email": "testuser@example.com"
    }
   Response Example:
    {
      "status": "success",
      "message": "You have successfully subscribed to the monthly newsletter."
    }
   
2) Check Subscription Status
   Endpoint: GET /subscription-status?email=
   Response Example:
    {
      "status": "success",
      "email": "user@example.com",
      "subscribed": true
    }
   
3) Update Email Address
   Endpoint: PUT /update-email
   Request Example:
    {
       "old_email": "testuser@example.com",
       "new_email": "newtestuser@example.com"
    }
   Response Example:
    {
       "status": "success",
       "message": "Your email has been updated successfully."
    }

4) Unsubscribe from Newsletter
   Endpoint: DELETE /unsubscribe
   Request Example:
     {
        "email": "newtestuser@example.com"
     }
   Response Example:
     {
        "status": "success",
        "message": "You have been unsubscribed successfully."
     }

5) Send Newsletter to all Subscribers
   Endpoint: POST /send-newsletter
   Response Example (Success):
    {
      "status": "success",
      "message": "Newsletter sent successfully."
    }
   Response Example (Failure):
    {
      "status": "error",
      "message": "Newsletter failed to send to some emails.",
      "failed_emails": "user3@example.com"
    }

---
**Customizing the Newsletter Content**
The default newsletter content is set in the send_newletter() function inside app.py 
<img width="672" alt="Screenshot 2025-02-24 at 4 40 40 PM" src="https://github.com/user-attachments/assets/2e8c4b96-31be-429e-b9e7-028f752340e8" />
To modify the email content, locate this function and update the subject and content variables. 

---
**TroubleShooting**
1) Microservice doesn't start
   This might be due to missing dependencies. Try running pip install -r requirements.txt
2) Emails not sending
   This might be due to incorrect Mailtrap Credentials. Verify your Mailtrap_user and mailtrap_pass
3) No response from API
   This could be due to the Flask not running. Ensure python app.py is running.



