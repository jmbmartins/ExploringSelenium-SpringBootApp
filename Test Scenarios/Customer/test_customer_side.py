import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

os.environ['PATH'] += r"C:\SeleniumDrivers"
driver = webdriver.Chrome()

driver.get('http://localhost:8080/')


# Test 1: Create a New Client
def register_client():
    try:

        driver.get('http://localhost:8080/')

        btnRegister = driver.find_element(By.ID, 'btnregister')
        btnRegister.click()

        driver.implicitly_wait(10)

        email_input = driver.find_element(By.NAME, 'email')
        password_input = driver.find_element(By.NAME, 'password')
        login_button = driver.find_element(By.ID, 'btnSub')

        email_input.send_keys('user3@example.com')
        password_input.send_keys('password3')
        login_button.click()

        time.sleep(2)

        driver.implicitly_wait(10)

        pagetitle_element = driver.find_element(By.ID, 'pagetitle')
        text = pagetitle_element.text

        assert "Welcome to Pet's Hotel," in text

        print("Test new client register succeeded!")
    except Exception as e:
        print("Test new client register failed:", str(e))


# Test 2: (Need to Log in First) Update Customer Personal Details
def update_customer_details():
    try:
        driver.get('http://localhost:8080/')

        email_input = driver.find_element(By.NAME, 'email')
        password_input = driver.find_element(By.NAME, 'password')
        login_button = driver.find_element(By.ID, 'btnSub')

        email_input.send_keys('user1@example.com')
        password_input.send_keys('password1')
        login_button.click()

        time.sleep(2)

        driver.implicitly_wait(10)

        btnUpdate = driver.find_element(By.CLASS_NAME, 'change-info-link')
        btnUpdate.click()

        name_input = driver.find_element(By.ID, "name")
        name_input.clear()
        name_input_mod = "John Does"
        name_input.send_keys(name_input_mod)

        adress_input = driver.find_element(By.ID, "add")
        adress_input.clear()
        add_input_mod = "123 Main Sts"
        adress_input.send_keys(add_input_mod)

        phone_input = driver.find_element(By.ID, "phone")
        phone_input.clear()
        phone_input_mod = "123-456-7891"
        phone_input.send_keys(phone_input_mod)

        btnSubmitChange= driver.find_element(By.ID, 'submit')
        btnSubmitChange.click()

        time.sleep(2)

        name_client_pos_change = driver.find_element(By.ID, "pageclient_name")
        add_client_pos_change = driver.find_element(By.ID, "pageclient_add")
        phone_client_pos_change = driver.find_element(By.ID, "pageclient_phone")

        assert ((name_client_pos_change.text == name_input_mod) and (add_client_pos_change.text == add_input_mod) and  (phone_client_pos_change.text == phone_input_mod))
        print("Test update client information succeeded")
    except Exception as e:
        print("Test update client information failed:", str(e))


# Main test scenario
try:
    # register_client()
    update_customer_details()
    # view_customer_information()
    # update_customer_details()
    # delete_customer()
except Exception as e:
    print(f"An error occurred: {str(e)}")
finally:
    driver.quit()  # Close the browser
