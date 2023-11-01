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


# Test 2: Insert personal data in a new client account
def insertdata_newclient():
    try:

        driver.get('http://localhost:8080/')

        email_input = driver.find_element(By.NAME, 'email')
        password_input = driver.find_element(By.NAME, 'password')
        login_button = driver.find_element(By.ID, 'btnSub')

        email_input.send_keys('user3@example.com')
        password_input.send_keys('password3')
        login_button.click()

        time.sleep(2)
        driver.implicitly_wait(10)

        # Find the input fields by their 'id' attribute
        txtbox_name = driver.find_element(By.ID, 'new_name')
        txtbox_address = driver.find_element(By.ID, 'new_address')
        txtbox_phone = driver.find_element(By.ID, 'new_phone')

        # Insert data for the frist time
        name = "Antonio Banderas"
        address = "Espanã"
        phone = "12-563-99"

        txtbox_name.send_keys(name)
        txtbox_address.send_keys(address)
        txtbox_phone.send_keys(phone)

        btnsub = driver.find_element(By.ID, 'newclientinfobtnsub')
        btnsub.click()

        # Check if already had been added the new information in client view
        name_client = driver.find_element(By.ID, "pageclient_name")
        add_client = driver.find_element(By.ID, "pageclient_add")
        phone_client = driver.find_element(By.ID, "pageclient_phone")

        assert ((name == name_client) and (phone == phone_client) and (address == add_client))
        print("Test insert personal data succeeded")
    except Exception as e:
        print("Test insert personal data failed:", str(e))


# Test 3: (Need to Log in First) Update Customer Personal Details
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

        btnSubmitChange = driver.find_element(By.ID, 'submit')
        btnSubmitChange.click()

        time.sleep(2)

        name_client_pos_change = driver.find_element(By.ID, "pageclient_name")
        add_client_pos_change = driver.find_element(By.ID, "pageclient_add")
        phone_client_pos_change = driver.find_element(By.ID, "pageclient_phone")

        assert ((name_client_pos_change.text == name_input_mod) and (add_client_pos_change.text == add_input_mod) and (
                phone_client_pos_change.text == phone_input_mod))
        print("Test update client information succeeded")
    except Exception as e:
        print("Test update client information failed:", str(e))


# Test 4: Remove a client (Admin)
def delete_customer():
    try:
        driver.get('http://localhost:8080/')

        email_input = driver.find_element(By.NAME, 'email')
        password_input = driver.find_element(By.NAME, 'password')
        login_button = driver.find_element(By.ID, 'btnSub')

        # Login with an admin account
        email_input.send_keys('manager@example.com')
        password_input.send_keys('managerpassword')
        login_button.click()

        time.sleep(2)

        driver.implicitly_wait(10)

        btnPageCustomers = driver.find_element(By.ID, 'btnPageHotelCustomers')
        btnPageCustomers.click()

        customer_name_to_delete = "Andres Iniesta"

        # Find all the rows in the table
        rows = driver.find_elements(By.CSS_SELECTOR, "table tbody tr")

        # Check if the customer exists in the list before deletion
        customer_exists_before_deletion = any(
            row.find_element(By.CSS_SELECTOR, "td:nth-child(2)").text == customer_name_to_delete for row in rows
        )

        # Loop through the rows to find the customer with the specified name
        for row in rows:
            name_cell = row.find_element(By.CSS_SELECTOR, "td:nth-child(2)")  # 2nd column has the customer name
            if name_cell.text == customer_name_to_delete:
                delete_link = row.find_element(By.LINK_TEXT, "Delete")
                delete_link.click()
                break

        # Check if the customer no longer exists in the list after deletion
        rows = driver.find_elements(By.CSS_SELECTOR, "table tbody tr")
        customer_exists_after_deletion = any(
            row.find_element(By.CSS_SELECTOR, "td:nth-child(2)").text == customer_name_to_delete for row in rows
        )

        # Assert that the customer has been deleted successfully
        assert customer_exists_before_deletion and not customer_exists_after_deletion, "Customer deletion failed"
        print("Test customer deletion succeeded")
    except Exception as e:
        print("Test Customer deletion failed:", str(e))


# Main test scenario
try:
    # register_client()
    # insertdata_newclient()
    # update_customer_details()
    delete_customer()
except Exception as e:
    print(f"An error occurred: {str(e)}")
finally:
    driver.quit()  # Close the browser
