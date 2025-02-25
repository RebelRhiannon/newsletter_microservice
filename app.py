from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import smtplib
from email.mime.text import MIMEText
import os

app = Flask(__name__)
CORS(app)  # Allows cross-origin requests

# file to store subscribers emails
SUBSCRIBERS_FILE = 'subscribers.json'


# Helper function to load subscribers safely
def load_subscribers():
    """
    Load the list of subscribers from the JSON file.
    If the file is empty or doesn't exist, return an empty list.
    """
    try:
        if not os.path.exists(SUBSCRIBERS_FILE) or os.stat(SUBSCRIBERS_FILE).st_size == 0:
            return []
        with open(SUBSCRIBERS_FILE, 'r') as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError):
        return []  # Return empty list instead of failing


# Helper function to save subscribers safely
def save_subscribers(subscribers):
    """
    Save the updated subscriber list to the JSON file.
    Ensures subscribers data is correctly written and saved.
    """
    if not isinstance(subscribers, list):
        print("Error: Subscribers list is corrupted.")
        return
    try:
        with open(SUBSCRIBERS_FILE, 'w') as file:
            json.dump(subscribers, file, indent=4)
    except IOError:
        print("Error: Could not write to subscribers.json")


# Function to send an email using Mailtrap SMTP (for testing)
def send_email(to_email, subject, content):
    """
    Sends an email using Mailtrap
    Requires MailTrap credentials to be set as environment variables.
    """

    # Use Mailtrap's SMTP credentials (set via environment variables)
    SMTP_SERVER = "smtp.mailtrap.io"
    SMTP_PORT = 2525
    SMTP_USER = os.getenv("MAILTRAP_USER")  # Set this in your environment
    SMTP_PASS = os.getenv("MAILTRAP_PASS")  # Set this in your environment

    if not SMTP_USER or not SMTP_PASS:
        return {"status": "error", "message": "Mailtrap SMTP credentials are missing."}

    msg = MIMEText(content)
    msg["Subject"] = subject
    msg["From"] = "newsletter@example.com"
    msg["To"] = to_email

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.login(SMTP_USER, SMTP_PASS)
            server.sendmail("newsletter@example.com", to_email, msg.as_string())
        return {"status": "success", "message": "Email sent successfully (test mode)."}
    except Exception as e:
        return {"status": "error", "message": str(e)}


# Route: Newsletter Signup
@app.route('/subscribe', methods=['POST'])
def subscribe():
    """
    API endpoint: Subscribe a new user to the newsletter.
    - Accepts an email address in the request body.
    - Returns 201 Created if the subscription is successful.
    - Returns 400 Bad Request if no email is provided
    - Returns 409 Conflict if the email is already subscribed.
    """
    data = request.get_json()
    email = data.get('email', '').strip().lower()  # Normalize email

    if not email:
        return jsonify({"status": "error", "message": "Email is required"}), 400

    subscribers = load_subscribers()

    if email in subscribers:
        return jsonify({"status": "error", "message": "Email is already subscribed"}), 409

    subscribers.append(email)
    save_subscribers(subscribers)

    return jsonify({"status": "success", "message": "You have successfully subscribed to the monthly newsletter."}), 201


# Route: Check Subscription Status
@app.route('/subscription-status', methods=['GET'])
def check_subscription_status():
    """
    API Endpoint: Check if a user is subscribed
    - Accepts an email as a query parameter
    - Returns 200 OK with subscription status
    - Returns 400 Bad Request if no email is provided
    """
    email = request.args.get('email', '').strip().lower()

    if not email:
        return jsonify({"status": "error", "message": "Email is required"}), 400

    subscribers = load_subscribers()

    if email in subscribers:
        return jsonify({"status": "success", "email": email, "subscribed": True}), 200
    else:
        return jsonify({"status": "success", "email": email, "subscribed": False}), 200


# Route: Unsubscribe from Newsletter
@app.route('/unsubscribe', methods=['DELETE'])
def unsubscribe():
    """
    API Endpoint: Unsubscribe a user from the newsletter.
    - Accepts an email in the request body.
    - Returns 200 OK if unsubscribed successfully
    - Returns 400 Bad Request if no email is provided
    - Returns 400 Not Found if the email does not exist in the list.
    """
    data = request.get_json()
    email = data.get('email', '').strip().lower()

    if not email:
        return jsonify({"status": "error", "message": "Email is required"}), 400

    subscribers = load_subscribers()

    if email not in subscribers:
        return jsonify({"status": "error", "message": "Email not found in the subscription list"}), 404

    subscribers.remove(email)
    save_subscribers(subscribers)

    return jsonify({"status": "success", "message": "You have been unsubscribed successfully."}), 200


# Route: Update Email Address
@app.route('/update-email', methods=['PUT'])
def update_email():
    """
    API Endpoint: Update a user's email address
    - Accepts Old_email and new_email in the request body.
    - Returns 200 OK if the update is successful.
    - Returns 400 Bad request if required fields are missing
    - Returns 404 Not Found if the old email is not found
    - Returns 409 Conflict if the new email is already subscribed.
    :return:
    """
    data = request.get_json()
    old_email = data.get('old_email', '').strip().lower()
    new_email = data.get('new_email', '').strip().lower()

    if not old_email or not new_email:
        return jsonify({"status": "error", "message": "Both old and new email addresses are required"}), 400

    subscribers = load_subscribers()

    if old_email not in subscribers:
        return jsonify({"status": "error", "message": "Old email not found in the subscription list"}), 404

    if new_email in subscribers:
        return jsonify({"status": "error", "message": "New email is already subscribed"}), 409

    subscribers.remove(old_email)
    subscribers.append(new_email)
    save_subscribers(subscribers)

    return jsonify({"status": "success", "message": "Your email has been updated successfully."}), 200


# Route: Send Monthly Newsletter (Mailtrap)
@app.route('/send-newsletter', methods=['POST'])
def send_newsletter():
    """
    Sends the newsletter to all subscribers (captured in Mailtrap inbox)
    API Endpoint: Send the newsletter to all subscribers
    - Fetches all subscribed emails
    - Sends the newsletter
    - Returns 200 OK if successful
    - Returns 400 Bad request if no subscribers exist
    """
    subscribers = load_subscribers()

    if not subscribers:
        return jsonify({"status": "error", "message": "No subscribers found"}), 400

    subject = "Monthly Cybersecurity Newsletter"
    content = "Your cybersecurity tips and news for this month!"

    failures = []

    for email in subscribers:
        result = send_email(email, subject, content)
        if result.get("status") == "error":
            failures.append(email)

    if failures:
        return jsonify({
            "status": "error",
            "message": "Newsletter failed to send to some emails.",
            "failed_emails": failures
        }), 500

    return jsonify({"status": "success", "message": "Newsletter sent successfully."}), 200


# Route: Health Check
@app.route('/health-check', methods=['GET'])
def health_check():
    return jsonify({"status": "running"}), 200


if __name__ == '__main__':
    app.run(debug=True)
