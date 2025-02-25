import requests
import json
import time

BASE_URL = "http://127.0.0.1:5000"


def test_subscribe(email):
    """ Test subscribing a user """
    url = f"{BASE_URL}/subscribe"
    data = {"email": email}

    start_time = time.time()
    response = requests.post(url, json=data)
    elapsed_time = round(time.time() - start_time, 3)

    print(f"\nTesting Subscribe ({email}) - Response Time: {elapsed_time} sec")
    print("Subscribe Response:", response.json())


def test_check_subscription(email):
    """ Test checking subscription status """
    url = f"{BASE_URL}/subscription-status?email={email}"

    start_time = time.time()
    response = requests.get(url)
    elapsed_time = round(time.time() - start_time, 3)

    print(f"\nTesting Check Subscription ({email}) - Response Time: {elapsed_time} sec")
    print("Subscription Status Response:", response.json())


def test_unsubscribe(email):
    """ Test unsubscribing a user """
    url = f"{BASE_URL}/unsubscribe"
    data = {"email": email}

    start_time = time.time()
    response = requests.delete(url, json=data)
    elapsed_time = round(time.time() - start_time, 3)

    print(f"\nTesting Unsubscribe ({email}) - Response Time: {elapsed_time} sec")
    print("Unsubscribe Response:", response.json())


def test_update_email(old_email, new_email):
    """ Test updating email address """
    url = f"{BASE_URL}/update-email"
    data = {"old_email": old_email, "new_email": new_email}

    start_time = time.time()
    response = requests.put(url, json=data)
    elapsed_time = round(time.time() - start_time, 3)

    print(f"\nTesting Update Email ({old_email} -> {new_email}) - Response Time: {elapsed_time} sec")
    print("Update Email Response:", response.json())


def test_send_newsletter():
    """ Test sending the newsletter to all subscribers """
    url = f"{BASE_URL}/send-newsletter"

    start_time = time.time()
    response = requests.post(url)
    elapsed_time = round(time.time() - start_time, 3)

    print(f"\nTesting Send Newsletter - Response Time: {elapsed_time} sec")
    print("Send Newsletter Response:", response.json())


if __name__ == "__main__":
    test_email = "testuser@example.com"
    new_email = "newtestuser@example.com"

    print("\n🔹 Running Test Program for Newsletter Microservice...\n")

    # Step 1: Test subscribing
    test_subscribe(test_email)

    # Step 2: Test checking subscription status
    test_check_subscription(test_email)

    # Step 3: Test updating email
    test_update_email(test_email, new_email)

    # Step 4: Test checking new email subscription status
    test_check_subscription(new_email)

    extra_email = "backupuser@example.com"
    test_subscribe(extra_email)

    extra_email = "backuser@example.com"
    test_subscribe(extra_email)

    # Step 7: Test sending the newsletter
    test_send_newsletter()

    # Step 5: Test unsubscribing
    test_unsubscribe(new_email)

    # Step 6: Check subscription status after unsubscribing
    test_check_subscription(new_email)

    test_check_subscription(extra_email)



