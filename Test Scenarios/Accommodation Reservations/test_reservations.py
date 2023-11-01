import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

os.environ['PATH'] += r"C:\SeleniumDrivers"
driver = webdriver.Chrome()

driver.get('http://localhost:8080/')


# Test 1: Make a reservation for a Pet
def make_reservation():
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


def delete_reservation():
    pass


def checkIn_after_checkOut():
    pass


def checkIn_before_currentDate():
    pass


# Main test scenario
try:
    make_reservation()
    delete_reservation()
    checkIn_after_checkOut()
    checkIn_before_currentDate()
except Exception as e:
    print(f"An error occurred: {str(e)}")
finally:
    driver.quit()  # Close the browser
