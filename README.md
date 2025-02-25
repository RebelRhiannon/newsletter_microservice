# newsletter_microservice - README

---
**Overview**

This microservice allows users to:
1) Subscribe to a monthly cybersecurity newsletter
2) Check their subscription status
3) Update their email address
4) Unsubscribe from the newsletter
5) Send the newsletter to all subscribers

It is built with Python (flask) and currently uses **Mailtrap SMTP** for email sending. 

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

<img width="343" alt="Screenshot 2025-02-24 at 4 50 33 PM" src="https://github.com/user-attachments/assets/6d2e5947-c656-47e6-be04-3e675c8faa2c" />


To verify:

<img width="507" alt="Screenshot 2025-02-24 at 4 50 53 PM" src="https://github.com/user-attachments/assets/fba489ed-23dd-4718-9048-02b22b49eda6" />


Windows

<img width="328" alt="Screenshot 2025-02-24 at 4 51 23 PM" src="https://github.com/user-attachments/assets/4fd1130f-fa18-4b73-a12b-b5546e85fbe4" />


To verify:

<img width="522" alt="Screenshot 2025-02-24 at 4 51 35 PM" src="https://github.com/user-attachments/assets/b7e5afcf-6833-4d85-8cfa-e9a75b06ee0d" />

---
**Running the Microservice**

Start the Flask server: Python app.py or (if using Python 3) python3 app.py

By Default: the server will run at http://127.0.0.1:5000/

---
**API Endpoints and Usage**
1) Subscribe to Newsletter, 
   Endpoint: POST/subscribe
   
   <img width="561" alt="Screenshot 2025-02-24 at 4 51 52 PM" src="https://github.com/user-attachments/assets/fab6ab6f-d92d-47e5-92ed-24f207ca5669" />

2) Check Subscription Status, 
   Endpoint: GET /subscription-status?email=
   
   <img width="390" alt="Screenshot 2025-02-24 at 4 52 09 PM" src="https://github.com/user-attachments/assets/7dfe474e-c418-4df7-94fc-1e8942e71180" />
   
3) Update Email Address, 
   Endpoint: PUT /update-email
   
   <img width="437" alt="Screenshot 2025-02-24 at 4 52 21 PM" src="https://github.com/user-attachments/assets/f7d07834-f69e-4551-bb6b-74bab418b2b9" />

4) Unsubscribe from Newsletter, 
   Endpoint: DELETE /unsubscribe
   
   <img width="435" alt="Screenshot 2025-02-24 at 4 52 33 PM" src="https://github.com/user-attachments/assets/4e017ca5-ec00-4207-bd08-7c50ab4a1b96" />

5) Send Newsletter to all Subscribers, 
   Endpoint: POST /send-newsletter
   
   <img width="429" alt="Screenshot 2025-02-24 at 4 52 45 PM" src="https://github.com/user-attachments/assets/84917cd6-4a83-4093-b8dd-44b68389b7fd" />

---
**Customizing the Newsletter Content**

The default newsletter content is set in the send_newletter() function inside app.py

<img width="672" alt="Screenshot 2025-02-24 at 4 40 40 PM" src="https://github.com/user-attachments/assets/2e8c4b96-31be-429e-b9e7-028f752340e8" />

To modify the email content, locate this function and update the subject and content variables. 

---
**Requesting Data from the Microservice (communication contract)**

The developer can request data using HTTP methods such as GET, POST, PUT, and Delete. 

Example: Subscribing a User

<img width="682" alt="Screenshot 2025-02-24 at 5 11 47 PM" src="https://github.com/user-attachments/assets/9f665a78-bdc2-4d33-bf36-a0a07531da4b" />

**Receiving Data from the Microservice (Communication Contract)**

Responses are returned in ***JSON format**. Developer must handle JSON parsing. 

Example: Checking Subscription Status

<img width="992" alt="Screenshot 2025-02-24 at 5 14 07 PM" src="https://github.com/user-attachments/assets/4c0126ff-8a0e-4026-8b1c-17ea6fb2ff93" />

---
**UML Sequence Diagram**

<img width="745" alt="Screenshot 2025-02-24 at 6 27 57 PM" src="https://github.com/user-attachments/assets/d4b8b7f3-fc47-4464-a4b2-965eb6a81dd1" />


---

**TroubleShooting**
1) Microservice doesn't start:
   
   This might be due to missing dependencies. Try running pip install -r requirements.txt
2) Emails not sending:
   
   This might be due to incorrect Mailtrap Credentials. Verify your Mailtrap_user and mailtrap_pass
3) No response from API:
   
   This could be due to the Flask not running. Ensure python app.py is running.

---







